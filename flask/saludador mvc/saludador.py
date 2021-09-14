from flask import Flask, render_template
from logica import saludo

app = Flask(__name__)

@app.route('/hola/<nombre>')
def inicio(nombre):
    data = {'dolar': 3800, 'euro': 4500, 'libra': 5500}
    return render_template('hola.html', saludo = saludo(nombre), info = data)


if __name__ == '__main__':
    app.run()
