from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flasgger import Swagger, swag_from
from product import productStore
from personStore import personStore
import productgen

# Set up CORS and Flask
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Configure the OpenAPI document
app.config['SWAGGER'] = {
    'specs_route': "/api/api-docs/",
    'title': 'IMB Product Store API',
    'openapi': '3.0.2',
    'version': '1.0',
    'uiversion': 3,
    'description': 'API for connecting to the Information Management Branch Product store. It allows devs to surface a current product list, along with relevant info, as well as devs and scrum masters working on products. Done for BC IMB code challange',
}
swagger = Swagger(app)

appStore = productStore()
employeeStore = personStore()

@app.route('/')

# --- api/health ---

# Repsond to health check call with status
@app.route("/api/health")
def healthCheck():
    return 'Status: Healthy', 200

# --- api/product ---

# Handle a request to add new item to the list of products
@app.route('/api/product',methods=['POST'])
@swag_from("./docs/api/product/post.yml")
def addNewProduct():
    raw = request.get_json()
    if appStore.checkName(raw['ProductName']):
        return "Error: This product name already exists, please use PUT with an ID if you want to edit", 409
    else:
        ID = appStore.addProduct(raw["ProductName"],raw["ProductOwnerName"],raw["Developers"],
                            raw["ScrumMasterName"],raw["StartDate"],raw["Methodology"]
                            )
        print("got ID"+ID)
        employeeStore.addDev(raw["Developers"], ID)
        employeeStore.addScrum(raw["ScrumMasterName"], ID)
        return 'Product added', 200

# Get a list of all products in the database
@app.route("/api/product", methods=['GET'])
@swag_from("./docs/api/product/get.yml")
def returnProdList():
    json_list = jsonify({"products": appStore.list()})
    return json_list,200

# Handle PUT without an ID [error]
@app.route("/api/product", methods=['PUT'])
def listPutError():
    return 'No ID provided to update', 400

# Clear the entire database on DELETE call
@app.route("/api/product", methods=['DELETE'])
@swag_from("./docs/api/product/delete.yml")
def deleteList():
    appStore.store.clear()
    return 'Database cleared', 200

# --- api/product/productID ---

# Return error if trying to post by ID
@app.route("/api/product/<string:prod_id>", methods=['POST'])
def idPostError():
    return ' ', 400

# Get a single product by ID
@app.route("/api/product/<string:prod_id>", methods=['GET'])
@swag_from("./docs/api/product/productID/get.yml")
def getbyID(prod_id):
    if not appStore.checkID(prod_id):
        return "Error: could not find the requested ID", 404
    else:
        product = appStore.getByID(prod_id)
        return jsonify(product), 200

# Given an ID, update a product in the store
@app.route("/api/product/<string:prod_id>", methods=['PUT'])
@swag_from("./docs/api/product/productID/put.yml")
def editByID(prod_id):
    if not appStore.checkID(prod_id):
        return "Error: could not find the requested ID", 404
    else:
        args = request.get_json()
        appStore.editByID(prod_id,args)
        return 'Updated', 200

# Given an ID, delete a product from the store
@app.route("/api/product/<string:prod_id>", methods=['DELETE'])
@swag_from("./docs/api/product/productID/delete.yml")
def deleteByID(prod_id):
    if not appStore.checkID(prod_id):
        return "Error: could not find the requested ID", 404
    else:
        appStore.deleteByID(prod_id)
        return 'deleted', 200

# --- api/employee

# get list of employees
@app.route("/api/employee", methods=['GET'])
@swag_from("./docs/api/employee/get.yml")
def listEmployees():
    employees = jsonify({"employees":employeeStore.list()})
    return employees, 200

@app.route("/api/employee", methods=['POST'])
def addEmployeeError():
    return 'Not yet implmented', 501

# --- api/employee/userID/developed

# get list of products an employee was dev on
@app.route("/api/employee/<string:name>/developed", methods=['GET'])
@swag_from("./docs/api/employee/name/developed/get.yml")
def getDevelopedByName(name):
    name = name.replace("_", " ")
    products = jsonify({"products":employeeStore.getDevProducts(name)})
    return products, 200

# These are not implmented as outside scope of extra points
@app.route("/api/employee/<string:name>/developed", methods=['DELETE'])
def deleteEmployeeDev(name):
    return 'Not yet implmented', 501

@app.route("/api/employee/<string:name>/developed", methods=['PUT'])
def editEmployeeDev(name):
    return 'Not yet implmented', 501

@app.route("/api/employee/<string:name>/developed", methods=['POST'])
def postEmployeeDev(name):
    return 'Not yet implmented', 501

# --- api/employee/userID/scrummed

# get list of products an employee was scrum master on
@app.route("/api/employee/<string:name>/scrummed", methods=['GET'])
@swag_from("./docs/api/employee/name/scrummed/get.yml")
def getScrummedByName(name):
    name = name.replace("_", " ")
    products = jsonify({"products":employeeStore.getScrumProducts(name)})
    return products, 200

# These are not implmented as outside scope of extra points
@app.route("/api/employee/<string:name>/scrummed", methods=['DELETE'])
def deleteEmployeeScrum(name):
    return 'Not yet implmented', 501

@app.route("/api/employee/<string:name>/scrummed", methods=['PUT'])
def editEmployeeScrum(name):
    return 'Not yet implmented', 501

@app.route("/api/employee/<string:name>/scrummed", methods=['POST'])
def postEmployeeScrum(name):
    return 'Not yet implmented', 501

if __name__ == '__main__':
    productgen.generateProducts(40,appStore, employeeStore)
    app.run(host="localhost", port=3000)
