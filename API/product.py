import hashlib
# Object for basic, temporary storage of products without a proper database system using python dict object
class productStore:
    # Use a dict to store each product by ID
    def __init__(self):
        self.store = {}
    
    # Add a new product to the dict using the productID
    def addProduct(self, Name:str, Owner:str, Devs:list[str], ScrumMaster:str, StartDate:str, Methodology:str):
        product = {}
        ID = hashlib.sha1(Name.encode()).hexdigest()
        product["ProductID"] = ID
        product["ProductName"] = Name
        product["ProductOwnerName"] = Owner
        product["Developers"] = Devs
        product["ScrumMasterName"] = ScrumMaster
        product["StartDate"] = StartDate
        product["Methodology"] = Methodology

        self.store[product["ProductID"]] = product
        return ID

    # Return all items in the dictionary
    def list(self):
        # return array of product details + count
        formatted = []
        for p in self.store.values():
            formatted.append(p)
        return formatted

    # Return a specific product given an ID
    def getByID(self, ID:hex):
        return self.store[ID]

    # Update a product given an ID
    def editByID(self, ID:hex, edits):
        for editItem in edits:
            self.store[ID][editItem] = edits[editItem]

    # Delete a product given an ID
    def deleteByID(self, ID:hex):
        del self.store[ID]

    # Check if a name is already in the product store, returns true if it is
    def checkName(self, testName:str):
        if hashlib.sha1(testName.encode()).hexdigest() in self.store:
            return True
        else:
            return False
        
    # Check if an ID is currently in the store
    def checkID(self, ID:hex):
        if ID in self.store: return True
        else: return False

    def getDevs(self, ID):
        return self.store[ID]["Developers"]

    def getScrum(self, ID):
        return self.store[ID]["ScrumMasterName"]
    

    def getName(self, ID):
        return self.store[ID]["ProductName"]