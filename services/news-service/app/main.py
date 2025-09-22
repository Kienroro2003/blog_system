# services/news-service/app/main.py

from app import create_app

app = create_app()

if __name__ == "__main__":
    # Gunicorn sẽ dùng biến 'app' này để chạy
    app.run(host="0.0.0.0", port=8000)
