from flask import Flask, redirect, render_template, request

from MongoDBClient import MongoDBClient
from TodoService import TodoService

app = Flask(__name__)

mongoClient = MongoDBClient("mongodb://root:password@localhost:27017/", "app")
todoService = TodoService(mongoClient)

@app.get("/")
def home():
    todos = todoService.listTodos()
    print(todos)
    return render_template("index.html", todos=todos)

@app.post("/todo/check")
def checkTodo():
    id = request.form['id']
    todoService.checkTodo(id)
    return redirect('/')

@app.post("/todo/uncheck")
def uncheckTodo():
    id = request.form['id']
    todoService.uncheckTodo(id)
    return redirect('/')

@app.post("/todo/delete")
def deleteTodo():
    id = request.form['id']
    todoService.deleteTodo(id)
    return redirect('/')

@app.post("/todo/add")
def addTodo():
    todoName = request.form['todoName']
    todoService.addTodo({
        'todo': todoName,
        'status': False
    })
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

