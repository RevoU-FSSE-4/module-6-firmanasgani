from employee.repositories.employee_repository import EmployeeRepository
from enum import Enum

class Schedules(Enum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class EmployeeSevice:
    def __init__(self, repository):
        self.repository: EmployeeRepository = repository

    def validate_employee(self, employee):
        name = employee.get("name")
        role = employee.get("role")
        scheduler = employee.get("scheduler")

        if not name or not isinstance(name, str) or not (5 < len(name) <=100):
            raise ValueError("Name must be a string and at least 5 characters long")
    
        if not role or not isinstance(role, str) or not (5 < len(role) <=100):
            raise ValueError("Role must be a string and at least 5 characters long")
        
        if scheduler not in [schedule.value for schedule in Schedules]:
             raise ValueError("Schedule must be one of: DAILY, WEEKLY or MONTHLY")
        
    def create_employee(self, employee):
        self.validate_employee(employee)
        return self.repository.save_employee(employee)
    
    def get_all(self):
        return self.repository.get_all()
    
    def get_employeee(self, id):
        return self.repository.get_employee(id)
    
    def delete_employee(self, id):
        return self.repository.delete_employee(id)
        
