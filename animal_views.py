from flask import Blueprint, request, jsonify
from flasgger import swag_from

animal_blueprint = Blueprint("animals", __name__)

tasks = []


@animal_blueprint.route("/tasks", methods=["GET"])
def get_tasks():
    """
    Get task list
    ---
    responses:
        200:
            description: A list of tasks
    """
    return jsonify({"tasks": tasks}), 200