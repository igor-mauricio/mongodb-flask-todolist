from abc import ABC, abstractmethod
from dataclasses import dataclass

from MongoDBClient import MongoDBClient

class TodoDAO(ABC):
    @abstractmethod
    def addTodo(self, todo): ...
    def listTodos(self) -> list: ...


@dataclass
class InMemoryTodoDAO(TodoDAO):
    todos: list

    def addTodo(self, todo):
        self.todos.append(todo)

    def listTodos(self) -> list:
        return self.todos


@dataclass
class MongoTodoDAO(TodoDAO):
    client: MongoDBClient

    def addTodo(self, todo):
        self.client.add('todo', todo)

    def listTodos(self) -> list:
        return self.client.findAll('todo')
    

    