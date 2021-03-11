from flask import Flask # importing flask
from models import Schema
app = Flask(__name__) # Create an app instance

@app.route("/") # at / endpoint do what - the what follows
def hello(): # call function hello
    return "Hello world" # which returns Hello world

@app.route("/<name>")
def hello_with_name(name):
    return "Hello, "+name

if __name__=='__main__': # whenever app.py is run, the flask app would be run
    Schema()
    app.run(debug=True)