from datetime import datetime
from typing import List, Tuple
import json
from collections import defaultdict
from itertools import groupby
from operator import itemgetter
import pandas as pd


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Carga los tweets en un DataFrame de pandas
    df = pd.read_json(file_path, lines=True)

    # Convierte la columna 'date' a tipo datetime para facilitar el manejo
    df['date'] = pd.to_datetime(df['date'])

    # Extrae la parte de la fecha (YMD) y agrégala como una nueva columna 'fecha'
    df['fecha'] = df['date'].dt.date

    # Agrupa los tweets por la columna 'fecha' y cuenta el número de tweets por fecha
    conteo_tweets_por_fecha = df.groupby('fecha').size()

    # Obtiene las top 10 fechas con más tweets
    top_fechas = conteo_tweets_por_fecha.nlargest(10)

    # Inicializa una lista para almacenar los resultados
    resultados = []

    # Procesa las top 10 fechas con más tweets
    for fecha, num_tweets in top_fechas.items():
        # Filtra los tweets correspondientes a esta fecha
        tweets_fecha = df[df['fecha'] == fecha]
        # Obtiene el usuario con más publicaciones para esta fecha
        usuario_mas_publicaciones = tweets_fecha['user'].value_counts().index[0]['username']
        resultados.append((fecha, usuario_mas_publicaciones))

    return resultados