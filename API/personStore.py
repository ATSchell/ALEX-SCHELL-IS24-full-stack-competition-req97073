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

    #TODO: Make this a proper return of products deved and SM'ed by each employee
    def list(self):
        return list(self.store.keys())
        
    def getDevProducts(self, name:str):
        return self.store[name].developed

    def getScrumProducts(self, name:str):
        return self.store[name].scrummed
              