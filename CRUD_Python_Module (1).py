from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        # Connection Variables
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Create error:", e)
                return False
        else:
            return False

    def read(self, query):
        # Search for documents in the animals collection
        if query is not None:
            try:
                result = self.collection.find(query)
                return list(result)
            except Exception as e:
                print("Read error:", e)
                return []
        else:
            return []
    def update(self, query, new_values):
        # Update documents in the animals collection
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except Exception as e:
                print("Update error:", e)
                return 0
        else:
            return 0

    def delete(self, query):
        # Delete documents from the animals collection
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Delete error:", e)
                return 0
        else:
            return 0

