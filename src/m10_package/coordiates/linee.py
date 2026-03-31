"""### Parte 3: Implementazione di `coordinate/linee.py`
Funzioni per gestire le linee (definite da due punti):

- `crea_linea(p1: dict, p2: dict) -> dict:` 
  - Restituisce un dizionario con chiavi: `p1`, `p2`

- `lunghezza_linea(linea: dict) -> float:` 
  - Calcola la lunghezza using `distanza_tra_punti`
  - Importa `from .punti import distanza_tra_punti`

- `punto_medio(linea: dict) -> dict:` 
  - Restituisce il punto medio tra p1 e p2
  - Coordinate: ((x1+x2)/2, (y1+y2)/2)
- `info_linea(linea: dict) -> str:` 
  - Restituisce formato: `"Linea da (x1, y1) a (x2, y2)"`
  """

# from .punti import distanza_tra_punti
from . import punti 

def crea_linea(p1: dict, p2: dict) -> dict: 

  dic_crea={
      "p1":(p1) ,
      "p2":(p2)
  }

  return dic_crea



def lunghezza_linea(linea: dict) -> float:

  risultato=punti.distanza_tra_punti(linea['p1'], linea['p2'])

  return risultato


def punto_medio(linea: dict) -> dict:

  x1=linea['p1']['x']
  x2=linea['p2']['x']
  y1=linea['p1']['y']
  y2=linea['p2']['y']

  

  

  dic={
      "x": (x1+x2)/2,
      "y": (y1+y2)/2
  }
  return dic




def info_linea(linea: dict) -> str:

  x1=linea['p1']['x']
  x2=linea['p2']['x']
  y1=linea['p1']['y']
  y2=linea['p2']['y']

  stringa=(f"Linea da ({x1}, {y1}) a ({x2}, {y2})")
  
  return stringa 