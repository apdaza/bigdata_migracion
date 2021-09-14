from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/succes/<nombre>')
def inicio(nombre):
    return "Hola %s" % nombre

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['nombre']
        return redirect(url_for('inicio', nombre = usuario))
    else:
        usuario = request.args.get('nombre')
        return redirect(url_for('inicio', nombre = usuario))

if __name__ == '__main__':
    app.run()
