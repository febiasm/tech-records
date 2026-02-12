from fastapi import APIRouter
from .routes import profile

api_router = APIRouter()
api_router.include_router(profile.router)
