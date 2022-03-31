from app.api import get_session
from fastapi import APIRouter, status, Depends, Query, HTTPException
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
from app.models import Tag


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_tag(*, session: Session = Depends(get_session), tag: Tag):
    print(tag)
    db_tag = Tag.from_orm(tag)
    session.add(db_tag)
    session.commit()
    session.refresh(db_tag)
    return db_tag


@router.get("/", status_code=status.HTTP_200_OK)
async def get_tags(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    tags = session.exec(select(Tag).offset(offset).limit(limit)).all()
    return tags


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_tag(
    *,
    session: Session = Depends(get_session),
    id: int,
):
    db_tag = session.get(Tag, id)
    if not db_tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag


@router.patch("/{id}", status_code=status.HTTP_201_CREATED)
async def update_tag(*, session: Session = Depends(get_session), id: int, tag: Tag):
    db_tag = session.get(Tag, id)
    if not db_tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    tag_data = tag.dict(exclude_unset=True)
    for key, value in tag_data.items():
        setattr(db_tag, key, value)
    session.add(db_tag)
    session.commit()
    session.refresh(db_tag)
    return db_tag


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_tag(*, session: Session = Depends(get_session), id: int):
    db_tag = session.get(Tag, id)
    if not db_tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    session.delete(db_tag)
    session.commit()
    return db_tag
