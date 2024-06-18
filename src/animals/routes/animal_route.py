from flask import Blueprint, request, jsonify
from animals.repositories.animals_repository import AnimalRepository
from animals.services.animals_services import AnimalService
from flasgger import swag_from

animal_routes = Blueprint("animal_route", __name__)
repository: AnimalRepository = AnimalRepository()
service: AnimalService = AnimalService(repository=repository)
print(__name__)

@animal_routes.route('/animals', methods=["GET"])
@swag_from('../docs/get_all_animals.yml')
def get_all():
    animals = service.get_all()
    return animals

@animal_routes.route('/animal/<int:id>', methods=["GET"])
@swag_from('../docs/get_animal.yml')
def get_aniaml(id):
    animals = service.get_animal(id)
    if animals is None:
        return {"Error": "animals not found"}, 404
    return animals


@animal_routes.route('/animals', methods=["POST"])
@swag_from('../docs/create_animal.yml')
def create_animal():
    animals = request.get_json()
    try:
        animals = service.create_animals(animals)
    except ValueError as e:
        return {"Error": str(e)}, 400

    return animals, 200   


@animal_routes.route('/animal/<int:id>', methods=["DELETE"])
@swag_from(
    {
        "tags": ["Animals"],
        "parameters": [
            {
                "in": "path",
                "name": "id",
                "schema": {"type": "integer"},
                "required": True,
                "description": "The animal ID",
            }
        ],
        "responses": {
            204: {"description": "animal deleted"},
            404: {"description": "animal not found"},
        },
    }
)
def delete_animal(id):
    animals = service.delete_animal(id)
    if animals is None: 
        return {"error": "Animal not found"}, 404

    return "", 204