from flask import Flask
from flask_cors import CORS
import felix

app = Flask(__name__)
CORS(app)
@app.route("/")
def hello_world():
    return "<p>Hello, World!!!</p>"

@app.route("/tweedeendpoint")
def hello_world1():
    return "Iets heel anders teruggeven"

@app.route("/derde/<onsgegeven>")
def hello_world3(onsgegeven):
    return "Dit is ons gegeven"+onsgegeven

@app.route("/felix")
def felixfunc():
    return felix.mijnfunctie()
