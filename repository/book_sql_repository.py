import sqlite3
from domain.use_cases import BookRepositoryInterface
from domain.entities import Book


class BookSQLRepository(BookRepositoryInterface):
    def __init__(self, db_path):
        self.db_path = db_path

    def _execute_query(self, query, params=None, is_select=False):
        """ Helper method to execute database queries with context management """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or [])
            if is_select:
                return cursor.fetchone()
            conn.commit()

    def add(self, book: Book):
        """ Add a new book to the database """
        self._execute_query(
            "INSERT INTO books (id, title, author, year) VALUES (?, ?, ?, ?)",
            (book.id, book.title, book.author, book.year)
        )

    def get_by_id(self, book_id):
        """ Retrieve a book by its ID """
        row = self._execute_query(
            "SELECT id, title, author, year FROM books WHERE id = ?",
            (book_id,), is_select=True
        )
        if row:
            return Book(id=row[0], title=row[1], author=row[2], year=row[3])
        return None
