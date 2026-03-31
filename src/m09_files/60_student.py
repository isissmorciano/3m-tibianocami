#!/usr/bin/env python3
"""Simple interactive menu for managing students (JSON storage).

No UUID, no argparse, no CSV, no os, no custom functions.
Pure menu-driven with for loops.
"""

import json

STORAGE_FILE = "studenti.json"


if __name__ == "__main__":

    # Caricamento iniziale
    try:
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            studenti = json.load(f)
            if not isinstance(studenti, list):
                studenti = []
    except (FileNotFoundError, json.JSONDecodeError):
        studenti = []

    while True:
        print("\n=== GESTIONE STUDENTI ===")
        print("1. Aggiungi studente")
        print("2. Visualizza lista")
        print("3. Visualizza dettaglio")
        print("4. Aggiorna voto")
        print("5. Cancella studente")
        print("6. Ricerca per nome")
        print("7. Filtra per voto")
        print("8. Esci")

        scelta = input("\nScelta (1-8): ").strip()

        if scelta == "1":
            nome = input("Nome studente: ").strip()
            if not nome:
                print("Errore: nome non può essere vuoto.")
                continue

            voto_str = input("Voto (0-10): ")
            try:
                voto = float(voto_str)
            except ValueError:
                print("Errore: voto deve essere un numero.")
                continue

            if voto < 0 or voto > 10:
                print("Errore: voto deve essere tra 0 e 10.")
                continue

            studenti.append({"nome": nome, "voto": voto})
            print(f"Aggiunto: {nome} con voto {voto}")

        elif scelta == "2":
            if not studenti:
                print("Nessuno studente.")
            else:
                for i in range(len(studenti)):
                    s = studenti[i]
                    print(f"{i}. {s['nome']} - Voto: {s['voto']}")

        elif scelta == "3":
            if not studenti:
                print("Nessuno studente.")
                continue

            for i in range(len(studenti)):
                s = studenti[i]
                print(f"{i}. {s['nome']} - Voto: {s['voto']}")

            indice_str = input("Indice: ")
            try:
                indice = int(indice_str)
            except ValueError:
                print("Errore: indice deve essere un numero.")
                continue

            if indice < 0 or indice >= len(studenti):
                print("Indice non valido.")
                continue

            s = studenti[indice]
            print(f"Nome: {s['nome']}")
            print(f"Voto: {s['voto']}")

        elif scelta == "4":
            if not studenti:
                print("Nessuno studente.")
                continue

            for i in range(len(studenti)):
                s = studenti[i]
                print(f"{i}. {s['nome']} - Voto: {s['voto']}")

            indice_str = input("Indice da aggiornare: ")
            try:
                indice = int(indice_str)
            except ValueError:
                print("Errore: indice deve essere un numero.")
                continue

            if indice < 0 or indice >= len(studenti):
                print("Indice non valido.")
                continue

            voto_str = input("Nuovo voto (0-10): ")
            try:
                voto = float(voto_str)
            except ValueError:
                print("Errore: voto deve essere un numero.")
                continue

            if voto < 0 or voto > 10:
                print("Errore: voto deve essere tra 0 e 10.")
                continue

            studenti[indice]["voto"] = voto
            print(f"Aggiornato: {studenti[indice]['nome']} con voto {voto}")

        elif scelta == "5":
            if not studenti:
                print("Nessuno studente.")
                continue

            for i in range(len(studenti)):
                s = studenti[i]
                print(f"{i}. {s['nome']} - Voto: {s['voto']}")

            indice_str = input("Indice da cancellare: ")
            try:
                indice = int(indice_str)
            except ValueError:
                print("Errore: indice deve essere un numero.")
                continue

            if indice < 0 or indice >= len(studenti):
                print("Indice non valido.")
                continue

            nome = studenti[indice]["nome"]
            studenti.pop(indice)
            print(f"Cancellato: {nome}")

        elif scelta == "6":
            termine = input("Termine di ricerca: ").strip().lower()
            if not termine:
                print("Errore: termine non può essere vuoto.")
                continue

            risultati = []
            for s in studenti:
                if termine in s["nome"].lower():
                    risultati.append(s)

            if not risultati:
                print("Nessuno studente trovato.")
            else:
                print(f"Trovato(i) {len(risultati)} risultato(i):")
                for s in risultati:
                    print(f"  {s['nome']} - Voto: {s['voto']}")

        elif scelta == "7":
            try:
                min_voto = float(input("Voto minimo (0-10): "))
                max_voto = float(input("Voto massimo (0-10): "))
            except ValueError:
                print("Errore: numero non valido.")
                continue

            if min_voto < 0 or min_voto > 10 or max_voto < 0 or max_voto > 10:
                print("Errore: voti devono essere tra 0 e 10.")
                continue

            if min_voto > max_voto:
                print("Errore: voto minimo > voto massimo.")
                continue

            risultati = []
            for s in studenti:
                if min_voto <= s["voto"] <= max_voto:
                    risultati.append(s)

            if not risultati:
                print("Nessuno studente in questo range.")
            else:
                print(f"Trovato(i) {len(risultati)} risultato(i):")
                for s in risultati:
                    print(f"  {s['nome']} - Voto: {s['voto']}")

        elif scelta == "8":
            with open(STORAGE_FILE, "w", encoding="utf-8") as f:
                json.dump(studenti, f, ensure_ascii=False, indent=4)
            print("Salvato. Arrivederci!")
            break

        else:
            print("Scelta non valida. Riprova.")