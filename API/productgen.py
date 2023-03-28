# Generate initial, randomized projects 
from product import productStore
from personStore import personStore
import datetime

# generate a number of inital products to have in the database, generated randomly 
def generateProducts(runs:int, store:productStore, people:personStore):
    for i in range(runs):
        Name = "testProd "+str(i)
        ID = store.addProduct(Name, "First Last",["test", "name", "x"],"Test Name","2023-03-31" ,"Agile")
        people.addDev(["test", "name", "x"], ID)
        people.addScrum("Test Name", ID)
    