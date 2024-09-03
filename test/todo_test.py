import pytest
from MongoDBClient import MongoDBClient
from TodoService import TodoService

@pytest.fixture(scope="function")
def mongoClient():
    mongoClient = MongoDBClient("mongodb://root:password@localhost:27017/", "test_db")
    yield mongoClient
    mongoClient.dropDatabase("test_db")
    mongoClient.disconnect()

def testShouldAddTodo(mongoClient):
    todoService = TodoService(mongoClient)
    todo = {
        "task": "Do the shower"
    }

    id = todoService.addTodo(todo)

    result = todoService.listTodos()
    assert len(result) == 1
    assert result[0]['task'] == "Do the shower"
    assert result[0]['_id'] == id


def testShouldCheckTodo(mongoClient):
    todoService = TodoService(mongoClient)
    todo = {
        "task": "Do the shower",
        "status": False
    }
    id = todoService.addTodo(todo)

    todoService.checkTodo(id)

    result = todoService.listTodos()
    assert result[0]['_id'] == id
    assert result[0]['status'] == True

def testShouldUncheckTodo(mongoClient):
    todoService = TodoService(mongoClient)
    todo = {
        "task": "Do the shower",
        "status": True
    }
    id = todoService.addTodo(todo)

    todoService.uncheckTodo(id)

    result = todoService.listTodos()
    assert result[0]['_id'] == id
    assert result[0]['status'] == False

def testShouldDeleteTodo(mongoClient):
    todoService = TodoService(mongoClient)
    todo = {
        "task": "Do the shower",
        "status": True
    }
    id = todoService.addTodo(todo)

    todoService.deleteTodo(id)

    result = todoService.listTodos()
    assert len(result) == 0