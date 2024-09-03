from pymongo import MongoClient


class MongoDBClient:
    def __init__(self, uri,  database = "app"):
        self.client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        self.setDatabase(database)
        
    def setDatabase(self, name: str):
        self.db = self.client[name]
    
    def findAll(self, collection: str) -> list:
        return list(self.db[collection].find({}))
    
    def find(self, collection: str, filter: dict) -> list:
        return list(self.db[collection].find(filter))
    
    def add(self, collection:str, object: dict):
        result = self.db[collection].insert_one(object)
        return result.inserted_id

    def delete(self, collection:str, filter: dict):
        self.db[collection].delete_many(filter)

    def update(self, collection:str, filter: dict, update: dict):
        self.db[collection].update_many(filter, update)

    def dropDatabase(self, database: str):
        self.client.drop_database(database)

    def disconnect(self):
        self.client.close()