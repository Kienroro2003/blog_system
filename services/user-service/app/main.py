# services/user-service/app/main.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/users/")
def read_root():
    return {"message": "👋 Hello from User Service"}
