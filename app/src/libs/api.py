import os

from fastapi import FastAPI
from routes.api import router as api_router
from starlette.middleware.cors import CORSMiddleware


def create_app():
    app = FastAPI(
        title="Simple FastAPI CRUD",
        description="Simple CRUD implementation using FastAPI",
        version="0.0.1",
        root_path=os.getenv("API_PATH"),
        docs_url="/",
        redoc_url="/docs",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    return app
