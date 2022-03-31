from fastapi import APIRouter

from app.api.v1 import asstd, image, tag


api_router = APIRouter()
api_router.include_router(asstd.router, prefix="/asstd", tags=["Assorted"])
api_router.include_router(image.router, prefix="/image", tags=["Images"])
api_router.include_router(tag.router, prefix="/tag", tags=["Tags"])
