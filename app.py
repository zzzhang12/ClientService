from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# Replace with the URL of your deployed Flask app
BOOKS_API_URL = os.getenv('BOOKS_API_URL')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def get_books():
    genre_query = request.args.get('genre')
    author_query = request.args.get('author')
    year_query = request.args.get('year')
    title_query = request.args.get('title')

    params = {
        'genre': genre_query,
        'author': author_query,
        'publication_year': year_query,
        'title': title_query
    }
    
    response = requests.get(BOOKS_API_URL, params=params)
    if response.ok:
        if response.ok:
            data = response.json()
        if 'message' in data:
            # If the message key is in the response, render a template with the message and books
            return render_template('books.html', message=data['message'], books=data['books'])
        else:
            # Normal book list rendering
            return render_template('books.html', books=data)
    else:
        return jsonify({'error': 'Could not retrieve books from the API'}), 500


if __name__ == '__main__':
    app.run(debug=True)
