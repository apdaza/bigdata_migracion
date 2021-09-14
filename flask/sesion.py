from flask import Flask, redirect, session, url_for, request

app = Flask(__name__)
app.secret_key = 'qwerty'

@app.route('/')
def inicio():
    if 'usuario' in session:
        nombre = session['usuario']
        return "usted está logeado como %s " % nombre
    else:
        return "usted no está logeado, dirigirse a <a href='/login'>login</a>"

@app.route('/login')
def login():
    session['usuario'] = 'alejandro'
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run()
