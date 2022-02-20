from flask import Flask

# Documentation: https://flask.palletsprojects.com/en/2.0.x/quickstart/
app = Flask(__name__)


# Demo for Flask
@app.route("/")
def hello_world():
    return "Hello, World!"
