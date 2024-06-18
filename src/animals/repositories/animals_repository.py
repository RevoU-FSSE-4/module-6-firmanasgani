class AnimalRepository:
    def __init__(self):
        self.animals = {}
        self.id = 1

    def get_all(self):
        return list(self.animals.values())
    
    def save_animals(self, animals):
        animals["id"] = self.id
        self.animals[self.id] = animals
        self.id += 1
        return animals
    
    def get_animal(self, id):
        print(self.animals)
        return self.animals.get(id)
    
    def delete_animal(self, id):
        return self.animals.pop(id, None)
    