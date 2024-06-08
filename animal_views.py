from flask import Blueprint, request, jsonify
from flasgger import swag_from

animal_blueprint = Blueprint("animals", __name__)

animals = [{
    "name": "dog"
}, {
    "name": "cat"
}]


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

@animal_blueprint.route("/api/animal/<int:index>", methods=["GET"])
def get_animal(index):
    """
    Get individual task
    ---
    parameters:
      - name: index
        in: path
        required: true
    responses:
      200:
        description: A single task
    """
    try:
        animal = animals[index]
        return jsonify({"animal": animal}), 200
    except IndexError:
        return jsonify({"error": "Animal not found"}), 404
