# services/search-service/app/main.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/search/")
def read_root():
    return {"message": "🔍 Hello from Search Service"}
