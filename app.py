from flask import Flask, jsonify, request

app = Flask(__name__)

# Beispiel-Daten
books = [
    {"id": 1, "title": "Python for Beginners", "author": "John Doe"},
    {"id": 2, "title": "Flask Cookbook", "author": "Jane Smith"}
]

# Eine GET-Routen, um alle Bücher abzurufen
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Eine GET-Routen, um ein bestimmtes Buch basierend auf der ID abzurufen
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Eine POST-Routen, um ein neues Buch hinzuzufügen
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = {
        "id": len(books) + 1,
        "title": data['title'],
        "author": data['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Eine PUT-Routen, um ein vorhandenes Buch zu aktualisieren
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Eine DELETE-Routen, um ein Buch zu löschen
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
