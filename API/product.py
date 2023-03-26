import hashlib
# Object for basic, temporary storage of products without a proper database system using python dict object
class productStore:
    # Use a dict to store each product by ID
    def __init__(self):
        self.store = {}
    
    # Add a new product to the dict using the productID
    def addProduct(self, Name:str, Owner:str, Devs:list[str], ScrumMaster:str, StartDate:str, Methodology:str):
        product = {}
        product["ProductID"] = hashlib.sha1(Name.encode()).hexdigest()
        product["ProductName"] = Name
        product["ProductOwnerName"] = Owner
        product["Developers"] = Devs
        product["ScrumMasterName"] = ScrumMaster
        product["StartDate"] = StartDate
        product["Methodology"] = Methodology

        self.store[product["ProductID"]] = product

    # Return all items in the dictionary
    def list(self):
        return list(self.store.values())

    # Return a specific product given an ID
    def getByID(self, ID:int):
        return self.store[ID]

    # Update a product given an ID
    def editByID(self, ID:int, edits):
        for editItem in edits:
            self.store[ID][editItem] = edits[editItem]

    # Delete a product given an ID
    def deleteByID(self, ID:int):
        del self.store[ID]