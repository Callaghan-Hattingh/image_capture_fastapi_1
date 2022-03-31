from app.api import get_session
from typing import List
from fastapi import APIRouter, status, Depends, Query, UploadFile, File, Form
from sqlmodel import Session, select
from app.models import Image
import shutil


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_images(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=5, lte=25),
):
    images = session.exec(select(Image).offset(offset).limit(limit)).all()
    return images


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_image(
    *,
    session: Session = Depends(get_session),
    files: List[UploadFile] = File(...),
    # image: Image,
    message: str = Form(...),
    tag: str = Form(...),
):
    for file in files:
        image = Image(
            image=file.filename,
            message=message,
            tag_id=tag,
        )
        session.add(image)
        session.commit()
        session.refresh(image)
        print(image)
        with open(f"static/{image.id}.png", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    return {"Result": "OK"}
