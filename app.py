from flask import Flask, request, jsonify

app = Flask(__name__)
app.debug = True
@app.route('/')
def hello_world(): 
    return '<p>Hello world!</p>'

@app.route('/books', methods=["GET", "POST"])
def books_helper():
    if request.method == "POST":
        # Create book here
        return {"message": "Create a new book"}
    else:
        # Retrieve list of books here
        return {"message": "Return list of books"}

# Animals routing
'''
    id: int,
    name: string,
    species: string,
    age: int,
    gender: string,
    
'''
# get /animals
@app.route('/animals', methods=["GET", "POST"])
def animals_holding():
    pass

@app.route("/animals/<int:animal_index>", methods=["GET", "PUT", "DELETE"])
def get_animal(animal_id):
    pass


#employee
@app.route('/employees', methods=["GET", "POST"])
def animals_holding():
    pass

@app.route("/employees/<int:employee_index>", methods=["GET", "PUT", "DELETE"])
def get_animal(animal_id):
    pass

