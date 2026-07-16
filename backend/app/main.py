from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.assistant_stream import router as stream_router
from app.api.v1.assistant import router as assistant_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    assistant_router,
    prefix="/api/v1",
)

app.include_router(
    stream_router,
    prefix="/api/v1",
)

@app.get("/")
def home():
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
    }