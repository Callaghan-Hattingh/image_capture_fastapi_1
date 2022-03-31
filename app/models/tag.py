from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from sqlalchemy import String
from sqlalchemy.sql.schema import Column




class TagBase(SQLModel):
    """
    Tag class
    """

    tag: str  # Field(sa_column=Column("name", String, unique=True))


class Tag(TagBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_time: datetime = Field(default=datetime.utcnow())
    images: List["Image"] = Relationship(back_populates="tag")
