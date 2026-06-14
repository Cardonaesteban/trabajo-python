from flask import Flask

app = Flask(__name__)

@app.route("/contacto")
def contacto():
    return "Contacto"


@app.route("/usuario/<nombre>")
def usuario(nombre):
    return f"Hola {nombre}"


app.run(debug=True)