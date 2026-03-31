# ### Parte 2: Modulo `domande.py`
#     Funzioni per gestire le domande (rappresentate come dizionari):
#     - `crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:`
#     - `risposta` è l'indice 0-based dell'opzione corretta

#     - `info_domanda(domanda: dict) -> str:`
#     - Restituisce una stringa leggibile con domanda + opzioni numerate

#     - `convalida_risposta(domanda: dict, scelta: int) -> bool:`
#     - Verifica se la scelta (1-based) è valida

#     - `verifica_risposta(domanda: dict, scelta: int) -> bool:`
#     - Restituisce True se la scelta (1-based) è corretta





def crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:
    

    #risposta` è l'indice 0-based dell'opzione corretta

    return {
        "testo": testo,
        "opzioni": opzioni,
        "risposta": risposta
    }


def info_domanda(domanda: dict) -> str:

    # Restituisce una stringa leggibile con domanda + opzioni numerate
    testo = domanda["testo"] + "\n"
    for i, opzione in enumerate(domanda["opzioni"], start=1):
        testo += f"{i}. {opzione}\n"
    return testo





def convalida_risposta(domanda: dict, scelta: int) -> bool:
    
    # Verifica se la scelta (1-based) è valida
    return 1 <= scelta <= len(domanda["opzioni"])

def verifica_risposta(domanda: dict, scelta: int) -> bool:

    # Restituisce True se la scelta (1-based) è corretta
    if not convalida_risposta(domanda, scelta):
        return False
    return scelta - 1 == domanda["risposta"]