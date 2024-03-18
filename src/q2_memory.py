from typing import List, Tuple
from collections import Counter
import emoji

#importo json para poder manejar datos en esa estructura
import json

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Estructura temporal para contar los emojis
    emojis_count = Counter()

    # Procesar los tweets
    with open(file_path, 'r', encoding='utf-8') as file:
         # Itero para leer por líneas el archivo json
         for line in file:

            # Cargo la línea leída
            tweet = json.loads(line)

            # Obtengo el texto del tweet
            text = tweet['content']

            # Extraigo lista de emojis en el texto
            emojis = [emoji['emoji'] for emoji in emoji.emoji_list(text)]
            # Actualizo la cuenta de emojis
            emojis_count.update(emojis)

    # Obtengo los top 10 emojis más usados
    top_10_emojis = emojis_count.most_common(10)
    
    return top_10_emojis