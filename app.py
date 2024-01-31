from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with the URL of your deployed Flask app
BOOKS_API_URL = 'http://zhangz-book-api-server.d5efebd7h9asdbg8.uksouth.azurecontainer.io:5000/books'

@app.route('/books', methods=['GET'])
def get_books():
    genre_query = request.args.get('genre')
    response = requests.get(BOOKS_API_URL)
    if response.ok:
        books = response.json()
        
        # If a genre query parameter is provided, filter books by genre
        if genre_query:
            books = [book for book in books if genre_query.lower() in book['genre'].lower()]

        # If no genre is specified, return the third book as default
        if not genre_query and len(books) >= 3:
            return jsonify(books[2])  # Return only the third book
        
        return jsonify(books)
    else:
        return jsonify({'error': 'Could not retrieve books from the API'}), 500

if __name__ == '__main__':
    app.run(debug=True)
