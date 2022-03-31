from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from .tag import Tag


class ImageBase(SQLModel):
    """
    Image class
    """

    message: Optional[str] = Field(default=None)
    # message: str
    image: Optional[str] = Field(default=None)
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id")
    deleted: Optional[bool] = Field(default=False)


class Image(ImageBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_time: datetime = Field(default=datetime.utcnow())
    tag: Optional[Tag] = Relationship(back_populates="images")
