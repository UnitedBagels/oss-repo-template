from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
client = MongoClient()

if __name__ == '__main__':

    # client = MongoClient('localhost', 27018)
    client = MongoClient('mongodb://localhost:27018/')

    db = client.mongo_db_lab

    definitions = db.definitions

    # Fetch all records
    for doc in definitions.find():
        pprint.pprint(doc)

    # Fetch one record
    pprint.pprint(definitions.find_one())

    # Fetch one specific record
    pprint.pprint(definitions.find_one({"word": "Couch Potato"}))

    # Fetch record by object id
    pprint.pprint(definitions.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8ce")}))

    # Insert and fetch record
    pprint.pprint(definitions.find_one({"word": "Penguin"}))  # First, make sure it already does not exist
    definitions.insert_one({"word": "Penguin", "definition": "One of the coolest animals on the planet."})
    pprint.pprint(definitions.find_one({"word": "Penguin"}))  # Check to make sure it was added correctly
