from flask import Blueprint, request, jsonify
from flasgger import swag_from
from repository import employees
from function import is_integer_id

empl_plueprint = Blueprint("employees", __name__)


@empl_plueprint.route("/api/employees", methods=["GET"])
def get_employees():
    """
    Get employee list
    ---
    responses: 
        200:
            description: a list of employee
    """

    return jsonify({"employee": employees}), 200


@empl_plueprint.route("/api/employee/<int:empl_id>", methods=["GET"])
def get_employee(empl_id):
    """
    Get individual employee
    ---
    parameters:
      - name: empl_id
        in: path
        required: true
    responses:
      200:
        description: A single employee
    """
    try:
        employee = list(filter(lambda employee: employee["id"] == empl_id, employees))
        return jsonify({"employee": employee}), 200
    except Exception as message: 
        return jsonify({"status": "Error", "Message": message}), 400
    
@empl_plueprint.route("/api/employee", methods=["POST"])
@swag_from("docs/employee/create_employee.yml")
def create_empl():
    """
    Added an employee
    ---
    """
    data = request.get_json()
    id = data.get("id")
    name = data.get("name")
    role = data.get("role")
    schedules = data.get("schedules")

    value = {
        "id": id,
        "name": name,
        "role": role,
        "schedules": schedules
    }

    schedules_type = ["daily", "weekly", "monthly"]
    if schedules not in schedules_type:
        return({"error": "Schedules must contain daily, weekly, or monthly"}), 400

    count = sum(1 for employee in employees if employee["id"] == id)
    if count == 1:
        return({"status": "error! id exists"}), 400
    elif id=="":
        return({"status": "error! id empty"}), 400
    elif is_integer_id(id):
        return({"status": "error! id must number"}), 400
    else:
        employees.append(value)
        return ({"status": "sucess added data", "employee": employees}), 201
    


@empl_plueprint.route("/api/employee", methods=["PUT"])
@swag_from("docs/employee/update_employee.yml")
def update_empl():
    """
    update an existing employee
    ---
    parameters:
      - name: empl_id
        in: path
        required: true
    """
    data = request.get_json()
    id = data.get("id")
    name = data.get("name")
    role = data.get("role")
    schedules = data.get("schedules")

    value = {
        "id": id,
        "name": name,
        "role": role,
        "schedules": schedules
    }

    global employees
    schedules_type = ["daily", "weekly", "monthly"]
    if schedules not in schedules_type:
        return({"error": "Schedules must contain daily, weekly, or monthly"}), 400

    count = sum(1 for employee in employees if employee["id"] == id)
    if count == 1:
        employee = list(filter(lambda employee: employee["id"] != id, employees))
        employees = [employee]
        employees.append(value)
        return jsonify({"employee": employees}), 201
    elif id=="":
        return({"status": "error! id empty"}), 400
    elif is_integer_id(id):
        return({"status": "error! id must number"}), 400
    else:
        return jsonify({"Error": "Error handling"}), 400
    
@empl_plueprint.route("/api/employee/<int:empl_id>", methods=["DELETE"])
def delete_empl(empl_id):
    """
    Delete employee  
    ---
    parameters:
      - name: empl_id
        in: path
        required: true
    responses:
      200:
        description: Delete employee based on employee id
      400:
        description: Error because paramaters
    """
    try:
        global employees
        employee = list(filter(lambda employee: employee["id"] != empl_id, employees))
        count = sum(1 for employee in employees if employee["id"] == empl_id)
        if count == 0:
            return jsonify({"status": f"id with {empl_id} not found"}), 400
        else:
            employees = [employee]
            return jsonify({"employee": employees, "status": f"employee with id {empl_id} is deleted"}), 200
    except Exception as message:
        return jsonify({"error": f"Emloyee not found: {message} "}), 400 