# services/news-service/app/utils/decorators.py

from functools import wraps

import jwt
from flask import current_app, jsonify, request


def reporter_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            # Chú ý: SECRET_KEY cần được đồng bộ với user-service
            data = jwt.decode(
                token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"]
            )
            roles = data.get("roles", [])
            if "reporter" not in roles:
                return jsonify({"message": "Reporter role required!"}), 403

            # Truyền user_id vào function để sử dụng
            kwargs["current_user_id"] = data["sub"]
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token is invalid!"}), 401

        return f(*args, **kwargs)

    return decorated
