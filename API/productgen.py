# Generate initial, randomized projects 
from product import productStore
import datetime

# generate a number of inital products to have in the database, generated randomly 
def generateProducts(runs:int, store:productStore):
    for i in range(runs):
        Name = "testProd "+str(i)
        store.addProduct(Name, "First Last",["test", "name", "x"],"Test Name","2023-03-31" ,"AGILE")
    