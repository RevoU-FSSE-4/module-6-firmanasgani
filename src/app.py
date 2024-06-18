from flask import Flask
from animals.routes.animal_route import animal_routes
from employee.routes.employee_routes import employee_route
from flasgger import Swagger

app = Flask(__name__)
app.register_blueprint(animal_routes)
app.register_blueprint(employee_route)
swagger = Swagger(app)

@app.route("/")
def home():
    return "OK"

@app.errorhandler(404)
def page_not_found(e):
    return {'message': 'The requested URL was not found on the server.'}, 404

if __name__ == '__main__':
    app.run(debug=True,port=3030)