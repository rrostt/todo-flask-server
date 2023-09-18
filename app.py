from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = [
    {
        "text": "En sak att göra",
        "done": False,
    },
    {
        "text": "Ta bort mig",
        "done": True,
    },
]

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/todos", methods=["GET"])
def getTodos():
    return todos

@app.route("/todos/<int:index>", methods=["PUT"])
def updateTodo(index):
    todos[index] = request.json
    return "hello"

@app.route("/todos", methods=["POST"])
def addTodo():
    todos.append(request.json)
    return todos
