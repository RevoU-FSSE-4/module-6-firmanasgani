from unittest.mock import MagicMock

import pytest
from animals.services.animals_services import AnimalService

@pytest.fixture
def service():
    repository = MagicMock()
    return AnimalService(repository)

@pytest.mark.parametrize(
    "animal, expected_exception",
    [
        (
            {
                "id": 1,
                "species": "t",
                "gender": "MALE",
                "age": 14,
                "special_req": "Special Requirement"
            },
            ValueError
        ),
        (
            {
                "id": 1,
                "species": "Species",
                "gender": "Jantan",
                "age": 14,
                "special_req": "Special Requirement"
            },
            ValueError
        ),
        (
            {
                "id": 1,
                "species": "species",
                "gender": "MALE",
                "age": "string",
                "special_req": "Special Requirement"
            },
            ValueError
        ),
        (
            {
                "id": 1,
                "species": "species",
                "gender": "MALE",
                "age": 14,
                "special_req": "t"
            },
            ValueError
        ),

    ]
)
def test_validate_animal(service, animal, expected_exception):
    with pytest.raises(expected_exception):
        service.validate_animal(animal)


def test_create_animal(service):
    animal = {
        "id": 1,
        "species": "Species",
        "gender": "MALE",
        "age": 4,
        "special_req": "Special Requirement"
    }

    service.repository.save_animals.return_value = animal
    result = service.create_animals(animal)
    service.repository.save_animals.assert_called_once_with(animal)
    assert result == animal

def test_get_post(service):
    animal = {
        "id": 1,
        "species": "Species",
        "gender": "MALE",
        "age": 4,
        "special_req": "Special Requirement"
    }

    service.repository.get_animal.return_value = animal
    result = service.get_animal(1)
    service.repository.get_animal.assert_called_once_with(1)
    assert result == animal

def test_delete_animal(service):
    animal = {
        "id": 1,
        "species": "Species",
        "gender": "MALE",
        "age": 4,
        "special_req": "Special Requirement"
    }
    service.repository.delete_animal.return_value = animal
    result = service.delete_animal(1)
    service.repository.delete_animal.assert_called_once_with(1)
    assert result == animal