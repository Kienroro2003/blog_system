# services/news-service/app/controllers/article_controller.py

from app.models.article import Article
from app.utils.db import db
from app.utils.decorators import reporter_required
from flask import Blueprint, jsonify, request

article_blueprint = Blueprint("articles", __name__)


@article_blueprint.route("/articles", methods=["POST"])
@reporter_required
def create_article(current_user_id):
    data = request.get_json()
    if not data or not all(k in data for k in ("title", "content")):
        return jsonify({"message": "Missing title or content"}), 400

    new_article = Article(
        title=data["title"], content=data["content"], author_id=current_user_id
    )

    # Thay thế list bằng việc lưu vào database
    db.session.add(new_article)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "Article created successfully!",
                "article": new_article.to_dict(),
            }
        ),
        201,
    )


@article_blueprint.route("/articles", methods=["GET"])
def get_articles():
    # Lấy tất cả bài viết từ database
    articles = Article.query.all()
    return jsonify([article.to_dict() for article in articles]), 200


@article_blueprint.route("/articles/<int:article_id>", methods=["GET"])
def get_article(article_id):
    # Lấy một bài viết theo ID
    article = Article.query.get_or_404(article_id)
    return jsonify(article.to_dict()), 200
