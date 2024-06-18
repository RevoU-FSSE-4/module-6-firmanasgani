class EmployeeRepository:
    def __init__(self):
        self.employee = {}
        self.id = 1

    def get_all(self):
        return list(self.employee.values())
    
    def save_employee(self, employee):
        employee["id"] = self.id
        self.employee[self.id] = employee
        self.id += 1
        return employee
    
    def get_employee(self, id):
        print(self.employee)
        return self.employee.get(id)
    
    def delete_employee(self, id):
        return self.employee.pop(id, None)
