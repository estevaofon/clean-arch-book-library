import __init__
from flask import Flask, request, jsonify
from domain.entities import Book
from repository.book_sql_repository import BookSQLRepository
from domain.use_cases import ManageBook


app = Flask(__name__)
# Assuming some db_connection is created here
db_path = 'library.db'
book_repository = BookSQLRepository(db_path)
book_manager = ManageBook(book_repository)


@app.route('/book', methods=['POST'])
def add_book():
    data = request.get_json()
    book = Book(**data)
    book_manager.add_book(book)
    return jsonify({"status": "success"}), 200


@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = book_manager.retrieve_book(book_id)
    return jsonify(book.__dict__), 200


if __name__ == '__main__':
    app.run(debug=True)
