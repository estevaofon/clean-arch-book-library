# Book Management System

This Book Management System is a Flask-based web application designed following the principles of Clean Architecture. It offers a simple API to manage books in a library, including adding new books and retrieving them by their ID.

## Project Structure

The project is structured as follows to maintain separation of concerns:

- `domain/`: Contains business entities (`entities.py`) and use cases (`use_cases.py`).
- `repository/`: Contains the repository interface (`book_repository.py`) and its SQLite implementation (`book_sql_repository.py`).
- `database/`: Manages database connections and schema initialization.
- `web/`: Flask application setup (`app.py`) and routes (`views.py`).

## Features

- Add books to the library.
- Retrieve books by ID.

## Technologies

- Python 3
- Flask
- SQLite