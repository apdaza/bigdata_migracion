from flask import Flask, render_template
from modelos.dashboard import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/imagenes/<tipo>')
def imagenes(tipo):
    url_img = None
    df = None
    if tipo == 'casos':
        url_img, df = resumen_casos()
    if tipo == 'contagio':
        url_img, df = resumen_contagio()
    if tipo == 'sexo':
        url_img, df = resumen_sexo()
    if tipo == 'edad':
        url_img, df = resumen_edad()
    else:
        url_img, df = resumen_dispersion()
        
    return render_template(
                    'imagenes.html',
                    imagen = url_img,
                    data = df.to_html(classes='data', header=True, index=False)
                    )


if __name__ == '__main__':
    app.run()
