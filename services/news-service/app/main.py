# services/news-service/app/main.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/news/")
def read_root():
    return {"message": "📰 Hello from News Service"}
