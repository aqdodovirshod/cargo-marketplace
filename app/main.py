from fastapi import FastAPI
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title="Cargo-Marketplace TJ-CN API",
        version="1.0.0",
        docs_url="/api/docs" if settings.ENVIRONMENT != "production" else None,
        redoc_url=None,
    )

    @app.get("/ping")
    async def ping():
        return {"status": "ok", "environment": settings.ENVIRONMENT}

    return app

app = create_app()