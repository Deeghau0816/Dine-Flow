from fastapi import FastAPI

from app.core.config import settings
from app.routers.categories import router as category_router


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

app.include_router(category_router)


@app.get("/")
def root():
    return {
        "message": "DineFlow API is running"
    }