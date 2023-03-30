import json
import os

# Used to help emulate databases, writes and reads to json files

# Given a filename and data, store json
def writeDatabase(fileName, data):
    fileExtended = fileName+".json"
    jsonData = json.dumps(data)
    with open(fileExtended, "w") as dataBase:
        dataBase.write(jsonData)
    
def readDatabase(fileName):
    data = {}
    fileExtended = fileName+".json"
    if (os.path.isfile(fileExtended)):
        with open(fileExtended, "r") as dataBase:
            data = json.load(dataBase)
    return data
