def scrivi_file(frasi, nome_file):
    
    with open(nome_file, 'w', encoding='utf-8') as file:
        for frase in frasi:
            file.write(frase + "\n")


def leggi_file(nome_file):
    
    righe = []
    with open(nome_file, 'r', encoding='utf-8') as file:
        for line in file:
            righe.append(line.strip())
    return righe


def main():
    
    frasi = ["Ciao mondo", "Python è divertente", "File handling"]

    nome_file = "esercizio56.txt"

    
    scrivi_file(frasi, nome_file)

    
    contenuto = leggi_file(nome_file)

    
    print("Contenuto del file:")
    for riga in contenuto:
        print(riga)


if __name__ == "__main__":
 main()
