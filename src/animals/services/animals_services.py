from animals.repositories.animals_repository import AnimalRepository
from enum import Enum

class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class AnimalService:

    def __init__(self, repository):
        self.repository: AnimalRepository = repository
    
    def validate_animal(self, animals):
        species = animals.get('species')
        age = animals.get("age")
        gender = animals.get("gender")
        special_req = animals.get("special_req")

        if not species or not isinstance(species, str) or not (5 < len(species) <= 100):
            raise ValueError("Species must be a string and at least 5 characters long")
        
        if not age or not isinstance(age, int) or not (0 < age < 1000):
            raise ValueError("Age must be integer and not below 0")
        
        if gender not in [gend.value for gend in Gender]:
            raise ValueError("Gender must be one of: MALE or FEMALE")
        
        if not special_req or not isinstance(special_req, str) or not (5 < len(special_req) <= 100): 
            raise ValueError("Special Requirement must be a string and at least 5 characters long")
        
    def create_animals(self, animals):
        self.validate_animal(animals)
        return self.repository.save_animals(animals)
        
    def get_all(self):
        return self.repository.get_all()
        
    def get_animal(self, id):
        return self.repository.get_animal(int(id))
        
    def delete_animal(self, id):
        return self.repository.delete_animal(int(id))