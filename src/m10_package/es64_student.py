"""
Parte 4: Utilizzo del package in `es64_reference.py`
    1. Crea alcune domande (almeno 3)
    2. Simula alcune risposte dell'utente
    3. Registra i risultati
    4. Stampa il riepilogo
    5. Salva su file e ricarica dall'archivio

    ## Concetti Chiave
    - **Package**: cartella con `__init__.py` e moduli
    - **Moduli collegati**: `risultati.py` usa `json` per la persistenza
    - **Funzioni pure**: funzioni che lavorano solo con dizionari e restituiscono risultati
    - **Gestione file**: lettura/scrittura JSON con gestione degli errori

    ## Esempio di Output
    ```
    Domanda: Qual è il linguaggio usato in questo corso?
    1. Python
    2. Java
    3. C++

    Risultati:
    Risposte corrette: 3/4 (75.0%)

    Risultati salvati in 'quiz_risultati.json'
    Risultati caricati: Risposte corrette: 3/4 (75.0%)
    ```
"""
from quiz1.domande import *

from quiz1.risultati import *
def main():
     
    """"Crea alcune domande (almeno 3)
        2. Simula alcune risposte dell'utente
        3. Registra i risultati
        4. Stampa il riepilogo
        5. Salva su file e ricarica dall'archivio
        """
    domanda=crea_domanda("Qual è il linguaggio usato in questo corso?", ["Python", "Java", "C++"], 0)
    print(f"Domanda: {domanda['testo']}")
    for i, opzione in enumerate(domanda["opzioni"], 1):
        print(f"{i}. {opzione}")
    
    risultati = crea_risultati()
    risposte_utente = [0, 1, 0, 2]
    for risposta in risposte_utente:
        corretta = (risposta == domanda["corretta"])
        registra_risposta(risultati, corretta)
    
    print("\nRisultati:")
    print(mostra_risultati(risultati))
    

    nome_file = 'quiz_risultati.json'
    salva_risultati(risultati, nome_file)
    print(f"\nRisultati salvati in '{nome_file}'")
    
    risultati_caricati = carica_risultati(nome_file)
    print(f"Risultati caricati: {mostra_risultati(risultati_caricati)}")

if __name__ == "__main__":
    main()
    