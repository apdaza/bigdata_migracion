from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def hola_admin():
    return "Hola admin"

@app.route('/invitado/<nombre>')
def hola_invitado(nombre):
    return "Hola %s como invitado" % nombre

@app.route('/usuario/<nombre>')
def hola_usuario(nombre):
    if nombre == 'admin':
        return redirect(url_for('hola_admin'))
    else:
        return redirect(url_for('hola_invitado', nombre = nombre))

if __name__ == '__main__':
    app.run()
