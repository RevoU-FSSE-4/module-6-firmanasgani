from flask import Blueprint, request, jsonify
from flasgger import swag_from

empl_plueprint = Blueprint("employee", __name__)
employee = {"name": "Jhon doe"}


@empl_plueprint.route("/api/employee", methods=["GET"])
def get_employee():
    """
    Get employee list
    ---
    responses: 
        200:
            description: a list of employee
    """

    return jsonify({"employee": employee}), 200