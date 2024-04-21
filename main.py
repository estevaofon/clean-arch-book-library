import sqlite3
from repository.book_sql_repository import BookSQLRepository
from domain.use_cases import ManageBook
from domain.entities import Book


db_path = 'library.db'
book_repository = BookSQLRepository(db_path)
book_manager = ManageBook(book_repository)

# Example of adding a book
new_book = Book(id=1, title="Clean Architecture", author="Robert C. Martin", year=2017)
book_manager.add_book(new_book)

# Example of retrieving a book
retrieved_book = book_manager.retrieve_book(1)
print(retrieved_book.title, retrieved_book.author)  # Should output: Clean Architecture Robert C. Martin
