# services/news-service/app/__init__.py

import os

from flask import Flask

from .controllers.article_controller import article_blueprint
from .models import article  # Import models
from .utils.db import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "your-super-secret-key"

    db.init_app(app)

    # Thêm đoạn này để tạo bảng trong database
    with app.app_context():
        db.create_all()

    app.register_blueprint(article_blueprint, url_prefix="/api/news")

    return app
