from typing import List, Tuple
import json
from collections import Counter
import re

def q2_time(file_path: str) -> List[Tuple[str, int]]:

    # Creo estructura para contar los emojis
    emojis_count = Counter()

    # Declaro filtro de expresión regular para buscar emojis codificados en formato \uXXXX
    filtro = re.compile(r'\\u[0-9a-fA-F]{4}')

    # Abro el archivo en modo lectura 
    with open(file_path, 'r', encoding='utf-8') as file:

        # Leo el archivo línea por línea
        for line in file:
            # Cargo la línea del archivo como un objeto JSON de manera laxa y usando un codificador personalizado
            tweet = json.loads(line, strict=False, object_hook=lambda d: {k: v.encode('unicode_escape').decode() if isinstance(v, str) else v for k, v in d.items()})
            # Extraigo solo el contenido del tweet
            text = tweet['content']
            # Buscar emojis codificados en formato \uXXXX
            emojis = filtro.findall(text)
            # Actualizo la cuenta de los distintos emojis
            emojis_count.update(emojis)

    # Obtengo los top 10 emojis más usados
    top_10_emojis = emojis_count.most_common(10)
    
    return top_10_emojis