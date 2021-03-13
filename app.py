from flask import Flask # importing flask
from flask import request, jsonify
from models import Schema
from services import ToDoService
app = Flask(__name__) # Create an app instance

@app.route("/") # at / endpoint do what - the what follows
def hello(): # call function hello
    return "Hello world" # which returns Hello world

# Adding todo invocation route via POST request
@app.route("/todo", methods=["POST"])
def create_todo():
    ToDoService().create(request.get_json())
    return ''

@app.route("/todo", methods=["GET"])
def select_todo():
    return jsonify(ToDoService().select(request.get_json))

if __name__=='__main__': # whenever app.py is run, the flask app would be run
    Schema()
    app.run(debug=True)