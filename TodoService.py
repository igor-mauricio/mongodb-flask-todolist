from dataclasses import dataclass

from MongoDBClient import MongoDBClient


@dataclass
class TodoService:
    mongoClient: MongoDBClient
    
    def addTodo(self, todo) -> str:
        return self.mongoClient.add('todo', todo)

    def listTodos(self) -> list:
        return self.mongoClient.findAll('todo')
    
    def checkTodo(self, id):
        self.mongoClient.updateFromId('todo', id, {"$set" : {"status": True}})
    
    def uncheckTodo(self, id):
        self.mongoClient.updateFromId('todo', id, {"$set" : {"status": False}})
    
    def deleteTodo(self, id):
        self.mongoClient.deleteFromId('todo', id)