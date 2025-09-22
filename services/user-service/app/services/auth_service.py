# services/user-service/app/services/auth_service.py

from datetime import datetime, timedelta

import jwt
from app.models.user import User
from app.utils.password_hasher import PasswordHasher
from flask import current_app


class AuthService:
    def authenticate(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user and PasswordHasher.verify(password, user.password_hash):
            return user
        return None

    def generate_token(self, user):
        payload = {
            "sub": user.id,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=1),
            "roles": [role.name for role in user.roles],
        }
        token = jwt.encode(
            payload, current_app.config["JWT_SECRET_KEY"], algorithm="HS256"
        )
        return token
