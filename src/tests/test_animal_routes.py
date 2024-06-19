import pytest
from flask import json
from unittest.mock import MagicMock

from app import app
from animals.routes import animal_route


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# def test_create_animals(client):
#     animal_route.services = MagicMock()
#     animal = {"id": 1, "species": "species animal", "gender": "MALE", "age": 16, "special_req": "Special Requirement"}
    
#     animal_route.service.create_animals.return_value = animal

#     response = client.post(
#         "/animals", data=json.dumps(animal), content_type="application/json"
#     )

#     animal_route.service.create_animals.assert_called_once_with(animal)
#     assert response.status_code == 200
#     assert json.loads(response.get_data()) == animal

def test_get_animal(client):
    animal_route.service = MagicMock()
    animal = {"id": 1, "species": "species animal", "gender": "MALE", "age": 16, "special_req": "Special Requirement"}
    animal_route.service.get_animal.return_value = animal
    response = client.get("/animal/1")
    animal_route.service.get_animal.assert_called_once_with(1)
    assert response.status_code == 200
    assert json.loads(response.get_data()) == animal

def test_delete_animal(client):
    animal_route.service = MagicMock()
    animal = {"id": 1, "species": "species animal", "gender": "MALE", "age": 16, "special_req": "Special Requirement"}
    animal_route.service.delete_animal.return_value = animal
    response = client.delete('/animal/1')
    animal_route.service.delete_animal.assert_called_once_with(1)
    assert response.status_code == 204