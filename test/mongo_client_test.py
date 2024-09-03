from random import random
from MongoDBClient import MongoDBClient


def testShouldCreateAndRetrieveData():
    mongoClient = MongoDBClient("mongodb://root:password@localhost:27017/", "test_db")

    data = {
        "name": "ayooooo",
        "random": random()
    }
    mongoClient.add('objs',data)
    assert data in mongoClient.findAll('objs')

    mongoClient.dropDatabase("test_db")
    mongoClient.disconnect()

