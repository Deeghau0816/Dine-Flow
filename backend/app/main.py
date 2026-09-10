from fastapi import FastAPI

from app.core.config import settings
from app.routers.health import router as health_router


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} is running"
    }