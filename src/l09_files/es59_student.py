"""# Esercizio 59: Gestione Inventario Prodotti

## Obiettivo
Gestire un inventario di prodotti in formato JSON, con funzioni per filtrare per categoria e calcolare il valore totale.

## Dati forniti
Una lista di prodotti hardcoded:
```python
prodotti = [
    {"nome": "Mela", "categoria": "Frutta", "prezzo": 2.5, "quantita": 10},
    {"nome": "Pane", "categoria": "Pane", "prezzo": 1.0, "quantita": 5},
    {"nome": "Banana", "categoria": "Frutta", "prezzo": 1.8, "quantita": 8}
]
```

## Istruzioni

1. **Definire `salva_inventario(prodotti, nome_file)`**: Accetta una lista di dizionari e un nome file. Salva la lista in JSON con indentazione.

2. **Definire `carica_inventario(nome_file)`**: Accetta un nome file e restituisce la lista di dizionari caricata da JSON.

3. **Definire `filtra_per_categoria(prodotti, categoria)`**: Accetta la lista prodotti e una stringa categoria. Restituisce una lista con i prodotti di quella categoria.

4. **Definire `calcola_totale_categoria(prodotti, categoria)`**: Accetta la lista prodotti e una categoria. Calcola e restituisce il valore totale (prezzo * quantita) per i prodotti di quella categoria.

5. **Definire `main()`**: 
   - Definisce `prodotti` (dati hardcoded)
   - Chiama `salva_inventario` su "inventario.json"
   - Chiama `carica_inventario` per ottenere i dati
   - Filtra per "Frutta" e calcola il totale
   - Stampa i prodotti filtrati e il totale

## Suggerimenti
- Importa `json`
- Usa `json.dump` e `json.load` come negli esercizi precedenti
- Per filtrare: usa un ciclo for e append se categoria corrisponde
- Per totale: somma prezzo*quantita solo per prodotti filtrati
- Gestisci errori di file (FileNotFoundError)

"""
import json

# 1. Salva inventario in un file JSON
def salva_inventario(prodotti, nome_file):
    try:
        with open(nome_file, "w") as file:
            json.dump(prodotti, file, indent=4)
        print(f"File '{nome_file}' salvato con successo.")
    except Exception as e:
        print(f"Errore nel salvataggio del file: {e}")

# 2. Carica inventario da un file JSON
def carica_inventario(nome_file):
    try:
        with open(nome_file, "r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non esiste.")
        return []
    except json.JSONDecodeError:
        print(f"Errore: il file '{nome_file}' non contiene un JSON valido.")
        return []

# 3. Filtra prodotti per categoria
def filtra_per_categoria(prodotti, categoria):
    filtrati = []
    for prodotto in prodotti:
        if prodotto["categoria"] == categoria:
            filtrati.append(prodotto)
    return filtrati

# 4. Calcola totale valore per categoria
def calcola_totale_categoria(prodotti, categoria):
    totale = 0
    prodotti_filtrati = filtra_per_categoria(prodotti, categoria)
    for prodotto in prodotti_filtrati:
        totale += prodotto["prezzo"] * prodotto["quantita"]
    return totale

# 5. Funzione main
def main():

    # Dati hardcoded
    prodotti = [
        {"nome": "Mela", "categoria": "Frutta", "prezzo": 2.5, "quantita": 10},
        {"nome": "Pane", "categoria": "Pane", "prezzo": 1.0, "quantita": 5},
        {"nome": "Banana", "categoria": "Frutta", "prezzo": 1.8, "quantita": 8}
    ]

    # Salva inventario su file
    salva_inventario(prodotti, "inventario.json")

    # Carica inventario da file
    inventario = carica_inventario("inventario.json")

    # Filtra per categoria "Frutta"
    frutta = filtra_per_categoria(inventario, "Frutta")
    print("Prodotti Frutta:", frutta)

    # Calcola totale valore frutta
    totale_frutta = calcola_totale_categoria(inventario, "Frutta")
    print("Totale valore Frutta:", totale_frutta)

# Esegui main
if __name__ == "__main__":
    main()
