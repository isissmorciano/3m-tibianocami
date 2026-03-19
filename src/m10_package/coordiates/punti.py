""""
### Parte 2: Implementazione di `coordinate/punti.py`
Funzioni per gestire i punti (rappresentati come dizionari): 

- `crea_punto(x: float, y: float) -> dict:` 
  - Restituisce un dizionario con chiavi: `x`, `y`

- `distanza_tra_punti(p1: dict, p2: dict) -> float:` 
  - Calcola la distanza euclidea tra due punti
  - Formula: √((x2-x1)² + (y2-y1)²)

- `info_punto(punto: dict) -> str:` 

  - Restituisce formato: `"(x, y)"`

  - Esempio: `"(3.5, 2.0)"`
"""

import math

def crea_punto(x: float, y: float) -> dict:

    dict_punto={}
    dict_punto["x"] = x
    dict_punto["y"] = y

    return dict_punto



def distanza_tra_punti(p1: dict, p2: dict) -> float:

    risultato=0

    x1= p1['x']
    y1= p1['y']

    x2= p2['x']
    y2= p2['y']

    risultato = (x2-x1)**2 + (y2-y1)**2

    risultato = math.sqrt(risultato)

    return risultato





def info_punto(punto: dict) -> str:

    x=punto.get('x', 0.0)
    y=punto.get('y', 0.0)  

    stringa= (x,y)


    return stringa
