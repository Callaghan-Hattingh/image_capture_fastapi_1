from fastapi import APIRouter, status
from datetime import datetime
from app.db import create_db_and_tables


router = APIRouter()


@router.on_event("startup")
def on_startup():
    create_db_and_tables()


@router.get("/time", status_code=status.HTTP_200_OK)
async def server_time():
    """
    Get the server time
    """
    return {"server time": datetime.now()}


@router.get("/api", status_code=status.HTTP_200_OK)
async def api_version():
    """
    Get the API version
    """
    return {"api-version": 0.1}
