from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola"

@app.route("/productos")
def productos():
    return "Productos"

app.run(debug=True)