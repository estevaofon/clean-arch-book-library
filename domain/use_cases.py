from domain.entities import Book
from repository.book_repository import BookRepositoryInterface


class ManageBook:
    def __init__(self, repository: BookRepositoryInterface):
        self.repository = repository

    def add_book(self, book: Book):
        # Additional business rules can be enforced here
        self.repository.add(book)

    def retrieve_book(self, book_id):
        return self.repository.get_by_id(book_id)
