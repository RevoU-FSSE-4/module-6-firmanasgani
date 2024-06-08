from flask import Blueprint, request, jsonify
from flasgger import swag_from
from repository import animals
from function import is_integer_id

animal_blueprint = Blueprint("animals", __name__)

#Get all animals
@animal_blueprint.route("/api/animals", methods=["GET"])
def get_animals():
    """
    Get animals list
    ---
    responses:
        200:
            description: A list of animals
    """
    
    return jsonify({"animals": animals}), 200


#Get animal by id
@animal_blueprint.route("/api/animal/<int:animal_id>", methods=["GET"])
def get_animal(animal_id):
    """
    Get individual animal
    ---
    parameters:
      - name: animal_id
        in: path
        required: true
    responses:
      200:
        description: A single animal
    """
    try:
        animal = list(filter(lambda animal: animal["id"] == animal_id, animals))
        return jsonify({"animal": animal}), 200
    except IndexError:
        return jsonify({"error": "Animal not found"}), 404  


#POST animals
@animal_blueprint.route("/api/animals", methods=["POST"])
@swag_from("docs/animals/create_animal.yml")
def create_animal():
    """
    Added a new animal
    ---
    """
    data = request.get_json()
    id = data.get("id")
    species = data.get("species")
    age = data.get("age")
    gender = data.get("gender")
    special_req = data.get("special_req")

    value = {
        "id": id,
        "species": species,
        "age": age,
        "gender": gender,
        "special_req": special_req
    }

    count = sum(1 for animal in animals if animal["id"] == id)
    if count == 1:
        return ({"status": "error! id exists"}), 400
    elif id=="":
        return ({"status": "error! id is empty"}), 400
    elif is_integer_id(id):
        return ({"status": "error! id must number"}), 400
    elif is_integer_id(age):
        return ({"status": "age is must number"}), 400
    else:
        animals.append(value)
        return ({"status": "sucess added data", "animals": animals}), 201
    

@animal_blueprint.route("/api/animals/<int:id>", methods=["PUT"])
@swag_from("docs/animals/update_animal.yml")
def update_animal(id):
    data = request.get_json()
    id = data.get("id")
    species = data.get("species")
    age = data.get("age")
    gender = data.get("gender")
    special_req = data.get("special_req")

    value = {
        "id": id,
        "species": species,
        "age": age,
        "gender": gender,
        "special_req": special_req
    }
    global animals
    count = sum(1 for animal in animals if animal["id"] == id)
    if count == 1:
        
        animal = list(filter(lambda animal: animal["id"] != id, animals))
        animals = [animal]
        animals.append(value)
        return jsonify({"animal": animals}), 201
        #return ({"status": "error! id exists"}), 400
    elif id=="":
        return ({"status": "error! id is empty"}), 400
    elif is_integer_id(id):
        return ({"status": "error! id must number"}), 400
    elif is_integer_id(age):
        return ({"status": "age is must number"}), 400
    else:
        #animals.append(value)
        return jsonify({"Error": "Error handling"}), 400

@animal_blueprint.route("/api/animal/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    """
    Delete animal 
    ---
    parameters:
      - name: animal_id
        in: path
        required: true
    responses:
      200:
        description: Delete animal based on animal id
    """
    try:
        global animals
        animal = list(filter(lambda animal: animal["id"] != animal_id, animals))
        count = sum(1 for animal in animals if animal["id"] == animal_id)
        if count == 0:
            return jsonify({"status": f"id with {animal_id} not found"}), 400
        else:
            animals = [animal]
            return jsonify({"animal": animals, "status": f"animal with id {animal_id} is deleted"}), 200
    except IndexError:
        return jsonify({"error": "Animal not found"}), 404  