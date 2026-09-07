from fastapi import FastAPI

from app.core.config import settings
from app.database.connection import test_connection


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)


@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} is running",
        "environment": settings.environment
    }


@app.get("/db-test")
def db_test():
    result = test_connection()

    return {
        "database": "connected",
        "result": result
    }