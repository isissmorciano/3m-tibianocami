
# ### Parte 3: Modulo `risultati.py`
#     Funzioni per gestire i risultati del quiz e per salvarli/caricarli su file JSON:
#     - `crea_risultati() -> dict:`
#     - Restituisce un dizionario con chiavi: `totale`, `corretti`

#     - `registra_risposta(risultati: dict, corretta: bool) -> None:`
#     - Aggiorna i totali

#     - `percentuale_corrette(risultati: dict) -> float:`
#     - Restituisce la percentuale di risposte corrette (1 decimale)

#     - `mostra_risultati(risultati: dict) -> str:`
#     - Restituisce una stringa leggibile del riepilogo

#     - `salva_risultati(risultati: dict, nome_file: str) -> None:`
#     - Salva i risultati in un file JSON
#     - `carica_risultati(nome_file: str) -> dict:`
#     - Carica i risultati da un file JSON

def crea_risultati() -> dict:

    """Restituisce un dizionario con chiavi: `totale`, `corretti`"""

    return {
        "totale": 0,
        "corretti": 0 
    }

def registra_risposta(risultati: dict, corretta: bool) -> None:

    """Aggiorna i totali"""

    risultati["totale"] += 1
    if corretta:
        risultati["corretti"] += 1


def percentuale_corrette(risultati: dict) -> float:

    """Restituisce la percentuale di risposte corrette (1 decimale)"""

    if risultati["totale"] == 0:
        return 0.0
    return round((risultati["corretti"] / risultati["totale"]) * 100, 1)        

def mostra_risultati(risultati: dict) -> str:                                   

    """Restituisce una stringa leggibile del riepilogo"""

    percentuale = percentuale_corrette(risultati)
    return f"Risposte corrette: {risultati['corretti']}/{risultati['totale']} ({percentuale:2f}%)" 



def salva_risultati(risultati: dict, nome_file: str) -> None:

    """Salva i risultati in un file JSON"""

    import json
    try:
        with open(nome_file, 'w') as f:
            json.dump(risultati, f)
    except IOError as e:
        print(f"Errore durante il salvataggio: {e}")

def carica_risultati(nome_file: str) -> dict:
    
    """Carica i risultati da un file JSON"""

    import json
    try:
        with open(nome_file, 'r') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Errore durante il caricamento: {e}")
        return crea_risultati()