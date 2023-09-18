from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "methods": ["GET", "PUT", "OPTIONS", "POST"],  # Allow OPTIONS for preflight
        "allow_headers": ["Content-Type", "Authorization"],
        'origins': '*'
    }
})
todos = [
    {
        "text": "Ta bort mig",
        "done": False,
    }
]

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/todos", methods=["GET"])
def getTodos():
    return todos

@app.route("/todos", methods=["POST"])
def addTodo():
    todos.append(request.json)
    return True

@app.route("/todos/<int:index>", methods=["PUT"])
def updateTodo(index):
    todos[index] = request.json

@app.route("/todos/<int:index>", methods=["GET"])
def getTodo(index):
    return todos[index]
