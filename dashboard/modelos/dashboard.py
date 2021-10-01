import pandas as pd
import matplotlib.pyplot as plt

import base64
import io

covid_df = pd.read_csv('Casos_positivos_de_COVID-19_en_Colombia.csv')


def resumen_casos():
    covid_df['Nombre departamento'] = covid_df['Nombre departamento'].str.upper()
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

    return url_img, df


def resumen_contagio():
    covid_df['Tipo de contagio'] = covid_df['Tipo de contagio'].str.upper()
    df = covid_df.groupby(['Tipo de contagio'])['ID de caso'].count().reset_index()
    df.columns = ['contagio', 'casos']
    df['total'] = df['casos'].sum()
    df['porcentaje']= df['casos']/df['total']*100
    df = df.sort_values('casos', ascending=False)
    
    df.index = df['contagio']
    df.plot.pie(
        y = 'porcentaje',
        legend=False,
        autopct='%1.1f%%',
        title="Porcentaje de casos por tipo de contagio",
        explode=(0.1, 0.1, 0.1, 0.1),
        shadow=True,
        startangle=0
    )

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    url_img = base64.b64encode(img.getvalue()).decode()

    return url_img, df

def resumen_sexo():
    covid_df['Sexo'] = covid_df['Sexo'].str.upper()
    df = covid_df.groupby(['Sexo'])['ID de caso'].count().reset_index()
    df.columns = ['sexo', 'casos']
    df['total'] = df['casos'].sum()
    df['porcentaje']= df['casos']/df['total']*100
    df = df.sort_values('casos', ascending=False)
    
    df.index = df['sexo']
    df.plot.pie(
        y = 'porcentaje',
        legend=False,
        autopct='%1.1f%%',
        title="Porcentaje de casos por sexo",
        explode=(0.1, 0.1),
        shadow=True,
        startangle=0
    )

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    url_img = base64.b64encode(img.getvalue()).decode()

    return url_img, df

def resumen_edad():
    df = covid_df['Edad'].value_counts()
    df.plot.hist()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    url_img = base64.b64encode(img.getvalue()).decode()

    return url_img, df.to_frame()

def resumen_dispersion():
    df = covid_df.groupby(['Nombre departamento'])['ID de caso'].count().reset_index()
    df.columns = ['departamento', 'casos']
    df.index = df['departamento']
    pd.plotting.lag_plot(df['casos'], lag=1)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    url_img = base64.b64encode(img.getvalue()).decode()

    return url_img, df
