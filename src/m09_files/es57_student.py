def conta_parole(nome_file):
    
    conteggio = {}

    with open(nome_file, "r", encoding="utf-8") as file:
        testo = file.read().lower()

    
    testo = testo.replace(".", " ").replace(",", " ")
 
    parole = testo.split()

    for parola in parole:
        if parola in conteggio:
            conteggio[parola] += 1
        else:
            conteggio[parola] = 1

    return conteggio


def stampa_conteggio(dizionario):
    
    print("Conteggio parole:")
    for parola, count in sorted(dizionario.items()):
        print(f"{parola}: {count}")


def main():
    testo = "Python è un linguaggio di programmazione. Python è semplice e potente."

    nome_file = "esercizio57.txt"

    
    with open(nome_file, "w", encoding="utf-8") as f:
        f.write(testo)

   
    conteggio = conta_parole(nome_file)
    stampa_conteggio(conteggio)


if __name__ == "__main__":
    main()