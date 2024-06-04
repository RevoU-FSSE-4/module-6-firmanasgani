from flask import Flask, request

app = Flask(__name__)
app.debug = True
@app.route('/')
def hello_world(): 
    return '<p>Hello world!</p>'

@app.route('/books')
def books_helper():
    return "get all books"