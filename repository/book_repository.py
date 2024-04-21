from abc import ABC, abstractmethod
from domain.entities import Book


class BookRepositoryInterface(ABC):
    @abstractmethod
    def add(self, book: Book):
        """
        Add a book to the repository.

        Args:
            book (Book): The book to add.
        """
        pass

    @abstractmethod
    def get_by_id(self, book_id):
        """
        Retrieve a book by its ID from the repository.

        Args:
            book_id (int): The ID of the book to retrieve.
        """
        pass
