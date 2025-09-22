# services/user-service/app/__init__.py

import os

from flask import Flask

from .controllers.auth_controller import auth_blueprint
from .utils.db import db, migrate


def create_app():
    app = Flask(__name__)

    # Cấu hình kết nối database từ biến môi trường
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "your-super-secret-key"  # Thay đổi key này

    # Khởi tạo db và migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Đăng ký blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/api/users")

    return app
