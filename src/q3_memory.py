from typing import List, Tuple
from collections import Counter
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Estructura temporal para contar las menciones de cada usuario
    menciones = Counter()

    # Abro el archivo en modo lectura
    with open(file_path, 'r', encoding='utf-8') as file:
        # Recorro el archivo línea por línea
        for line in file:
            # Guardo el json del tweet de la línea actual
            tweet = json.loads(line)
            # Obtengo los usuarios mencionados en el tweet
            usuarios_mencionados = tweet.get('mentionedUsers', [])
            # Me aseguro de que hayan usuarios mencionados en el tweet
            if usuarios_mencionados != None:
                # Recorro cada uno de los usuarios mencionados
                for user in usuarios_mencionados:
                    # Obtengo el username del usuario mencionado de la iteración actual
                    usuario = user.get('username')
                    # Incremento las menciones para el usuario
                    menciones[usuario] += 1

    # Obtener los top 10 usuarios más influyentes
    top_10_usuarios = menciones.most_common(10)
    
    return top_10_usuarios
