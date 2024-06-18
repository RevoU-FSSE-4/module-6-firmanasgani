from flask import Blueprint, request, jsonify
from employee.repositories.employee_repository import EmployeeRepository
from employee.services.employee_services import EmployeeSevice
from flasgger import swag_from

employee_route = Blueprint("employee_route", __name__)
repository: EmployeeRepository = EmployeeRepository()
service: EmployeeSevice = EmployeeSevice(repository=repository)


@employee_route.route('/employees', methods=["GET"])
@swag_from('../docs/get_all_employee.yml')
def get_all():
    employee = service.get_all()
    return employee

@employee_route.route('/employee/<int:id>', methods=["GET"])
@swag_from('../docs/get_employee.yml')
def get_aniaml(id):
    employee = service.get_employeee(id)
    if employee is None:
        return {"Error": "Employee not found"}, 404
    return employee


@employee_route.route('/employees', methods=["POST"])
@swag_from('../docs/create_employee.yml')
def create_employee():
    employee = request.get_json()
    try:
        employee = service.create_employee(employee)
    except ValueError as e:
        return {"Error": str(e)}, 400

    return employee, 200   


@employee_route.route('/employees/<int:id>', methods=["DELETE"])
@swag_from(
    {
        "tags": ["Employee"],
        "parameters": [
            {
                "in": "path",
                "name": "id",
                "schema": {"type": "integer"},
                "required": True,
                "description": "The employee ID",
            }
        ],
        "responses": {
            204: {"description": "employee deleted"},
            404: {"description": "employee not found"},
        },
    }
)
def delete_employee(id):
    employee = service.delete_employee(id)
    if employee is None: 
        return {"error": "Employee not found"}, 404

    return "", 204