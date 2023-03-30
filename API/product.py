import hashlib
import databaseHandler

# Object for basic, temporary storage of products without a proper database system using python dict object
class productStore:
    # Use a dict to store each product by ID
    def __init__(self):
        self.store = {}

    def storeDatabase(self, database):
        databaseHandler.writeDatabase("products", database)

    def readDatabase(self):
        test = databaseHandler.readDatabase("products")
        return test
    
    # Add a new product to the dict using the productID
    def addProduct(self, Name:str, Owner:str, Devs:list[str], ScrumMaster:str, StartDate:str, Methodology:str):
        currentDB = self.readDatabase()
        product = {}
        ID = hashlib.sha1(Name.encode()).hexdigest()
        product["ProductID"] = ID
        product["ProductName"] = Name
        product["ProductOwnerName"] = Owner
        product["Developers"] = Devs
        product["ScrumMasterName"] = ScrumMaster
        product["StartDate"] = StartDate
        product["Methodology"] = Methodology

        currentDB[product["ProductID"]] = product
        self.storeDatabase(currentDB)
        return ID

    # Return all items in the dictionary
    def list(self):
        # return array of product details + count
        test = self.readDatabase()
        formatted = []
        for p in test.values():
            formatted.append(p)
        return formatted

    # Return a specific product given an ID
    def getByID(self, ID:hex):
        currentDB = self.readDatabase()
        return currentDB[ID]

    # Update a product given an ID
    def editByID(self, ID:hex, edits):
        currentDB = self.readDatabase()
        for editItem in edits:
            currentDB[ID][editItem] = edits[editItem]
        self.storeDatabase(currentDB)

    # Delete a product given an ID
    def deleteByID(self, ID:hex):
        currentDB = self.readDatabase()
        del currentDB[ID]
        self.storeDatabase(currentDB)

    # Check if a name is already in the product store, returns true if it is
    def checkName(self, testName:str):
        currentDB = self.readDatabase()
        if hashlib.sha1(testName.encode()).hexdigest() in currentDB:
            return True
        else:
            return False
        
    # Check if an ID is currently in the store
    def checkID(self, ID:hex):
        currentDB = self.readDatabase()
        if ID in currentDB: return True
        else: return False

    def getDevs(self, ID):
        currentDB = self.readDatabase()
        return currentDB[ID]["Developers"]

    def getScrum(self, ID):
        currentDB = self.readDatabase()
        return currentDB[ID]["ScrumMasterName"]
    

    def getName(self, ID):
        currentDB = self.readDatabase()
        return currentDB[ID]["ProductName"]