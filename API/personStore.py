from flask import jsonify
# Stores people and the projects they developed or were scrum master on
import databaseHandler

class person:
    def __init__(self):
        self.developed = []
        self.scrummed = []
        
class personStore:
    # store for getting products 
    def __init__(self):
        self.store = {}

    def storeDatabase(self, database):
        databaseHandler.writeDatabase("employees", database)

    def readDatabase(self):
        test = databaseHandler.readDatabase("employees")
        return test
        
    # for a given name, add product if they're already in the store
    # otherwise we make a new person object and add 
    def addDev(self, names:str, product):
        currentDB = self.readDatabase()
        items ={
            "developed":[],
            "scrummed": []
        }
        for name in names:
            # check if dev in storage
            if name in currentDB:
                currentDB[name]["developed"].append(product)
                #currentDB[name].developed.append(product)
            else:
                #newDev = person()
                items["developed"].append(product)
                currentDB[name] = items
                #newDev.developed.append(product)
                #currentDB[name] = newDev

        self.storeDatabase(currentDB)

    def addScrum(self, name:str, product):
        items ={
            "developed":[],
            "scrummed": []
        }
        # check if dev in storage or we need new object
        currentDB = self.readDatabase()
        if name in currentDB:
            currentDB[name]["scrummed"].append(product)
        else:
            items["scrummed"].append(product)
            currentDB[name] = items
        
        self.storeDatabase(currentDB)

    # remove a product from a developer
    def removeDev(self, name, product):
        currentDB = self.readDatabase()
        if name not in currentDB:
            pass
        else:
            currentDB[name]["developed"].remove(product)
        self.storeDatabase(currentDB)

    def removeScrum(self, name:str, product):
        currentDB = self.readDatabase()
        if name not in currentDB:
            pass
        else:
            currentDB[name]["scrummed"].remove(product)

        self.storeDatabase(currentDB)   

    # For use when modifying devs on a product, removes and add product to dev's lists as needed
    def editDev(self, oldDevs, newDevs, product):
        added = list(set(newDevs)-set(oldDevs))
        removed = list(set(oldDevs)-set(newDevs))
        self.addDev(added, product)
        for dev in removed:
            self.removeDev(dev,product)

    # Change list of scrummed products for handoff between two SMs
    def editScrum(self, oldScrum, newScrum, product):
        if oldScrum != newScrum:
            self.removeScrum(oldScrum, product)
            self.addScrum(newScrum,product)
        
    # Return list of users
    def list(self):
        currentDB = self.readDatabase()
        return list(currentDB.keys())
        
    # Return a list of productIDs developed by the user
    def getDevProducts(self, name:str):
        currentDB = self.readDatabase()
        return currentDB[name]["developed"]
    
    # Return a list of productIDs scrummed by the user
    def getScrumProducts(self, name:str):
        currentDB = self.readDatabase()
        return currentDB[name]["scrummed"]
    
    # check if a user is in the database
    def checkUser(self, name:str):
        currentDB = self.readDatabase()
        return (name in currentDB)
              