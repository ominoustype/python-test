from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int | None = None


class Book(BookCreate):
    id: int
