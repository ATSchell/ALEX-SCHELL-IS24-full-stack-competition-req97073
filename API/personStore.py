from flask import jsonify
# Stores people and the projects they developed or were scrum master on

class person:
    def __init__(self):
        self.developed = []
        self.scrummed = []
        
class personStore:
    # store for getting products 
    def __init__(self):
        self.store = {}
    
    # for a given name, add product if they're already in the store
    # otherwise we make a new person object and add 
    def addDev(self, names:str, product):
        for name in names:
            # check if dev in storage
            if name in self.store:
                self.store[name].developed.append(product)
            else:
                newDev = person()
                newDev.developed.append(product)
                self.store[name] = newDev

    def addScrum(self, name:str, product):
        # check if dev in storage or we need new object
        if name in self.store:
            self.store[name].scrummed.append(product)
        else:
            newDev = person()
            newDev.scrummed.append(product)
            self.store[name] = newDev

    # remove a product from a developer
    def removeDev(self, name, product):
        if name not in self.store:
            pass
        else:
            self.store[name].developed.remove(product)

    def removeScrum(self, name:str, product):
        if name not in self.store:
            pass
        else:
            self.store[name].scrummed.remove(product)

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
        return list(self.store.keys())
        
    # Return a list of productIDs developed by the user
    def getDevProducts(self, name:str):
        return self.store[name].developed
    
    # Return a list of productIDs scrummed by the user
    def getScrumProducts(self, name:str):
        return self.store[name].scrummed
    
    # check if a user is in the database
    def checkUser(self, name:str):
        return (name in self.store)
              