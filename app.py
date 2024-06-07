from flask import Flask, request, jsonify
from datetime import datetime
from animal_views import animal_blueprint
from flasgger import Swagger



app = Flask(__name__)
app.register_blueprint(animal_blueprint)

swagger = Swagger(app)


@app.before_request
def start_timer():
    request.start_time = datetime.now()

@app.after_request
def log_time(response):
    end_time = datetime.now()
    request_time = (end_time - request.start_time).total_seconds()
    print(f"Request time: {request_time} seconds")
    return response

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Route not found"}), 404