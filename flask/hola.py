from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Hola mundo"

@app.route('/flask')
def flask():
    return "Hola mundo en flask"

@app.route('/hola/<nombre>')
def hola(nombre):
    return "hola " + nombre

@app.route('/hola/<nombre>/<int:cantidad>')
def hola_cantidad(nombre, cantidad):
    return "hola " + (nombre * cantidad)

if __name__ == '__main__':
    app.run()
