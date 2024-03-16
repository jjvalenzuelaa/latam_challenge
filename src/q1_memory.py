#importo datetime para manejar las fechas
from datetime import datetime

#importo list y tuple para definir los tipos de dato
from typing import List, Tuple

#importo json para poder manejar datos en esa estructura
import json

#importo defaultdict para inicializar de forma automática nuevos valores
from collections import defaultdict

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    # Creo "tabla temporal" para contar los tweets por fecha. Con defaultdict si una fecha no existe se inicializa con cero
    tweets_por_fecha = defaultdict(int)

    # Creo "tabla temporal anidada" para guardar agrupados los tweets por usuario por fecha y poder contarlos luego
    usuario_mas_publicaciones_por_fecha = defaultdict(lambda: defaultdict(int))

    # Procesar los tweets
    # Abro el archivo .json en modo lectura y con with para que se cierre al terminar de leer.
    with open(file_path, 'r', encoding='utf-8') as file:
        #realizo lectura línea por línea. Primero traté de leerlo como 1 solo json y no funcionó, se debía leer cada línea por separado.
        for line in file:
            #cargo en un objeto json la línea actual
            tweet = json.loads(line)
            #obtengo la fecha de cada tweet extrayendo solo la parte de la fecha (omitiendo la hora)
            fecha = datetime.strptime(tweet['date'][:10], "%Y-%m-%d").date()
            #incremento el contador de tweets para la fecha del tweet actual
            tweets_por_fecha[fecha] += 1

            # obtengo el usuario del tweet actual
            usuario = tweet['user']['displayname']
            # incremento el contador de tweets para el usuario actual en la fecha actual
            usuario_mas_publicaciones_por_fecha[fecha][usuario] += 1

    # Obtengo las 10 fechas con más tweets ordenando por cantidad de manera descendente y tomando los primeros 10 registros
    top_10_fechas = sorted(tweets_por_fecha.items(), key=lambda x: x[1], reverse=True)[:10]

    resultados = []
    # Declaro un arreglo para guardar el resultado

    # Recorro las 10 fechas con más tweets obtenidas anteriormente
    for fecha, _ in top_10_fechas:
        # Obtengo los usuarios para la fecha del "registro" actual
        usuarios = usuario_mas_publicaciones_por_fecha[fecha]

        # Obtengo el usuario con más publicaciones para la fecha del "registro" actual
        usuario_mas_publicaciones = max(usuarios, key=usuarios.get)

        # Agrego al arreglo de resultado la fecha y el usuario con más publicaciones para esa fecha
        resultados.append((fecha, usuario_mas_publicaciones))

    return resultados