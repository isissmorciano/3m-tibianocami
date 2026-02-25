import json


def salva_studenti(studenti, nome_file):
    
    with open(nome_file, "w", encoding="utf-8") as file:
        json.dump(studenti, file, indent=4)
    print(f"File '{nome_file}' salvato con successo.")


def carica_studenti(nome_file):
   
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            studenti = json.load(file)
        return studenti
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non esiste.")
        return []


def calcola_media(studenti):
    
    if not studenti:
        return 0.0

    somma_voti = sum(studente["voto"] for studente in studenti)
    return somma_voti / len(studenti)


def main():
    studenti = [
        {"nome": "Alice", "voto": 8},
        {"nome": "Bob", "voto": 7},
        {"nome": "Carlo", "voto": 9}
    ]

    nome_file = "studenti.json"

   
    salva_studenti(studenti, nome_file)

  
    studenti_caricati = carica_studenti(nome_file)
    media = calcola_media(studenti_caricati)

    
    print("Studenti caricati:", studenti_caricati)
    print("Media voti:", media)


if __name__ == "__main__":
    main()