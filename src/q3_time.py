from typing import List, Tuple
import json
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
   # Defino estructura para almacenar los nombres de usuario únicos
    usuarios = set()
    # Defino estructura para contar el número de menciones por usuario
    menciones = Counter()

    # Abro el archivo en modo lectura
    with open(file_path, 'r', encoding='utf-8') as file:
        # Recorro el archivo línea por línea
        for line in file:
            #Guardo el tweet de la línea actual
            tweet = json.loads(line)
            # Obtengo los usuarios mencionados en el tweet
            usuarios_mencionados = tweet.get('mentionedUsers', [])
            # Me aseguro de contar solo cuando los tweets tienen menciones a usuarios
            if usuarios_mencionados != None:
                # Recorro los usuarios mencionados
                for user in usuarios_mencionados:
                    #obtengo cada usuario mencionado
                    usuario = user.get('username')
                    # Agregar el nombre de usuario al conjunto de usuarios únicos
                    usuarios.add(usuario)
                    # Incrementar el contador de menciones para este usuario
                    menciones[usuario] += 1

    # Obtengo los top 10 usuarios más mencionados
    # ordenando por el número total de menciones en orden descendente
    top_10_users = [(usuario, cantidad) for usuario, cantidad in menciones.most_common(10)]
    
    return top_10_users
