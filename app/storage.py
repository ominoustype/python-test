from app.schemas import Book, BookCreate


class BookStorage:
    def __init__(self) -> None:
        self._books: dict[int, Book] = {}
        self._next_id = 1

    def list(self) -> list[Book]:
        return list(self._books.values())

    def get(self, book_id: int) -> Book | None:
        return self._books.get(book_id)

    def create(self, data: BookCreate) -> Book:
        book = Book(id=self._next_id, **data.model_dump())
        self._books[book.id] = book
        self._next_id += 1
        return book

    def update(self, book_id: int, data: BookCreate) -> Book | None:
        if book_id not in self._books:
            return None
        book = Book(id=book_id, **data.model_dump())
        self._books[book_id] = book
        return book

    def delete(self, book_id: int) -> bool:
        return self._books.pop(book_id, None) is not None


storage = BookStorage()
