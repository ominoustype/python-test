from fastapi import APIRouter, HTTPException, Response, status

from app.schemas import Book, BookCreate
from app.storage import storage

router = APIRouter(prefix="/books", tags=["books"])


@router.get("", response_model=list[Book])
def list_books():
    return storage.list()


@router.post("", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(data: BookCreate):
    return storage.create(data)


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = storage.get(book_id)
    if book is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Book not found")
    return book


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, data: BookCreate):
    book = storage.update(book_id, data)
    if book is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Book not found")
    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    if not storage.delete(book_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Book not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
