from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flasgger import Swagger, swag_from
from product import productStore
from personStore import personStore
import productgen
import re

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
    if (raw['Methodology'] != "Agile") and (raw['Methodology'] != "Waterfall"):
        return "Error: Please use Agile or Waterfall as your methodology", 400
    dateCheck = re.compile("^[0-9]{4}\\/[0-9]{1,2}\\/[0-9]{1,2}$")
    if not (dateCheck.match(raw["StartDate"])):
        return "Error: Date not correctly formatted, please use YYYY/MM/DD", 400
    
    if appStore.checkName(raw['ProductName']):
        return "Error: This product name already exists, please use PUT with an ID if you want to edit", 409
    else:
        ID = appStore.addProduct(raw["ProductName"],raw["ProductOwnerName"],raw["Developers"],
                            raw["ScrumMasterName"],raw["StartDate"],raw["Methodology"]
                            )
        employeeStore.addDev(raw["Developers"], ID)
        employeeStore.addScrum(raw["ScrumMasterName"], ID)
        print(ID)
        return jsonify({"ID":ID}), 200

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
        # Check to ensure new data fits standards for storage
        if "Methodology" in args and ((args['Methodology'] != "Agile") and (args['Methodology'] != "Waterfall")):
            return "Error: Please use Agile or Waterfall as your methodology", 400
        dateCheck = re.compile("^[0-9]{4}\\/[0-9]{1,2}\\/[0-9]{1,2}$")

        if "StartDate" in args and not (dateCheck.match(args["StartDate"])):
            return "Error: Date not correctly formatted, please use YYYY/MM/DD", 400
        
        # Check for name collision, but allow for non-edit of name
        if "ProductName" in args and (args["ProductName"] != appStore.getName(prod_id)):
            if appStore.checkName(args['ProductName']):
                return "Error: This product name already exists, please use PUT with an ID if you want to edit", 409
            
        # get old and new devs to compare 
        oldDevs = appStore.getDevs(prod_id)
        oldScrum = appStore.getScrum(prod_id)
        # do the edit itself to the product in storage
        appStore.editByID(prod_id,args)
        newDevs = appStore.getDevs(prod_id)
        newScrum = appStore.getScrum(prod_id)
        employeeStore.editDev(oldDevs, newDevs, prod_id)
        employeeStore.editScrum(oldScrum,newScrum,prod_id)
        return 'Updated', 200

# Given an ID, delete a product from the store
@app.route("/api/product/<string:prod_id>", methods=['DELETE'])
@swag_from("./docs/api/product/productID/delete.yml")
def deleteByID(prod_id):
    if not appStore.checkID(prod_id):
        return "Error: could not find the requested ID", 404
    else:
        # get the list of devs and the srum master to remove this product from
        developers = appStore.getDevs(prod_id)
        scrumMaster = appStore.getScrum(prod_id)
        # delete the product
        appStore.deleteByID(prod_id)
        # remove product from all devs that worked on it
        for dev in developers:
            employeeStore.removeDev(dev,prod_id)
        employeeStore.removeScrum(scrumMaster, prod_id)
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
    if not employeeStore.checkUser(name):
        return jsonify({"products":[]}), 200
    name = name.replace("_", " ")
    productIDs = employeeStore.getDevProducts(name)
    developedProducts = []
    for ID in productIDs :
        developedProducts.append(appStore.getByID(ID))
    return jsonify({"products":developedProducts}), 200

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
    if not employeeStore.checkUser(name):
        return jsonify({"products":[]}), 200
    name = name.replace("_", " ")
    productIDs = employeeStore.getScrumProducts(name)
    scrummedProducts = []
    for ID in productIDs:
        scrummedProducts.append(appStore.getByID(ID))
    return jsonify({"products":scrummedProducts}), 200

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
