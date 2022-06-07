from turtle import title
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/books')
def get_books():    
    books = [
    { 'id': 1, 'title': 'Clean Code', 'authors': 'Robert C. Martin' },
    { 'id': 2, 'title': 'The DevOps Handbook', 'authors': 'Gene Kim, Jez Humble, Patrick Debois, John Willis' },
    { 'id': 3, 'title': 'The Phoenix Project', 'authors': 'Gene Kim, Kevin Behr,George Spafford' }
]
    booknames ={}
    for b in books:
        booknames["Name"] = (b["title"])
    return (booknames)
# Code to fetch all books from the database and return their details.

@app.route('/books/<id>')
def get_book(id): # Code to fetch the book entry with matching id from the database and return its details.
    return