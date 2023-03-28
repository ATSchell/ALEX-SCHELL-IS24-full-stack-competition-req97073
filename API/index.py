from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from product import productStore
from personStore import personStore
import productgen

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

appStore = productStore()
employeeStore = personStore()

# --- api/health ---

# Repsond to health check call with status
@app.route("/api/health")
def healthCheck():
    return 'Status: Healthy', 200

# --- api/product ---

# Handle a request to add new item to the list of products
@app.route('/api/product',methods=['POST'])
def addNewProduct():
    raw = request.get_json()
    if appStore.checkName(raw['ProductName']):
        return "Error: This product name already exists, please use PUT with an ID if you want to edit", 400
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
def returnProdList():
    json_list = jsonify({"products": appStore.list()})
    return json_list,200

# Handle PUT without an ID [error]
@app.route("/api/product", methods=['PUT'])
def listPutError():
    return 'No ID provided to update', 400

# Clear the entire database on DELETE call
@app.route("/api/product", methods=['DELETE'])
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
def getbyID(prod_id):
    if not appStore.checkID(prod_id):
        return "Error: could not find the requested ID", 400
    else:
        product = appStore.getByID(prod_id)
        return jsonify(product), 200

# Given an ID, update a product in the store
@app.route("/api/product/<string:prod_id>", methods=['PUT'])
def editByID(prod_id):
    if not appStore.checkID(prod_id):
        return "Error: could not find the requested ID", 400
    else:
        args = request.get_json()
        appStore.editByID(prod_id,args)
        return 'Updated', 200

# Given an ID, delete a product from the store
@app.route("/api/product/<string:prod_id>", methods=['DELETE'])
def deleteByID(prod_id):
    if not appStore.checkID(prod_id):
        return "Error: could not find the requested ID", 400
    else:
        appStore.deleteByID(prod_id)
        return 'deleted', 200

# --- api/employee

# get list of employees
@app.route("/api/employee", methods=['GET'])
def listEmployees():
    employees = jsonify({"employees":employeeStore.list()})
    return employees, 200

# get list of products an employee was dev on
@app.route("/api/employee/<string:name>/developed", methods=['GET'])
def getDevelopedByName(name):
    name = name.replace("_", " ")
    products = jsonify({"products":employeeStore.getDevProducts(name)})
    return products, 200

# get list of products an employee was scrum master on
@app.route("/api/employee/<string:name>/scrummed", methods=['GET'])
def getScrummedByName(name):
    name = name.replace("_", " ")
    products = jsonify({"products":employeeStore.getScrumProducts(name)})
    return products, 200

if __name__ == '__main__':
    productgen.generateProducts(40,appStore, employeeStore)
    app.run(host="localhost", port=3000)
