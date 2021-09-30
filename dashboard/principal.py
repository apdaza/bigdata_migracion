from flask import Flask, render_template

import pandas as pd
import matplotlib.pyplot as plt

import base64
import io

covid_df = pd.read_csv('Casos_positivos_de_COVID-19_en_Colombia.csv')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/imagenes/<tipo>')
def imagenes(tipo):
    if tipo == 'casos':
        df = covid_df.groupby(['Nombre departamento'])['ID de caso'].count().reset_index()
        df.columns = ['departamento', 'casos']
        df['total'] = df['casos'].sum()
        df['porcentaje']= df['casos']/df['total']*100
        df = df.sort_values('casos', ascending=False)
        df = df.head(5)

        df.index = df['departamento']
        df.plot.pie(
            y = 'porcentaje',
            legend=False,
            autopct='%1.1f%%',
            title="Departamentos con mayor número de casos",
            explode=(0.1, 0.1, 0.1, 0.1, 0.1),
            shadow=True,
            startangle=0
        )

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        url_img = base64.b64encode(img.getvalue()).decode()

    return render_template(
                    'imagenes.html',
                    imagen = url_img,
                    data = df.to_html(classes='data', header=True, index=False)
                    )


if __name__ == '__main__':
    app.run()
