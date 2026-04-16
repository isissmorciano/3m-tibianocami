from diario.entrate import *
from diario.persistenza import *

def main() :
    entrata1=crea_entrata("2026-04-08" , "studio" , 60 , "Ho iniziato un nuovo corso di Python.")
    entrata2=crea_entrata("2026-04-08" , "studio" , 45 , "Ho scritto un esercizio sul package diario.")
    entrata3=crea_entrata("2026-04-09" , "tempo libero" , 30 , "Sono andato a fare una passeggiata nel parco.")

    z=crea_diario()

    aggiungi_entrata(z, entrata1)
    aggiungi_entrata(z, entrata2)
    aggiungi_entrata(z, entrata3)
    
    
    print ("=== Diario ===")
    for i in z['entrate']:
        print(info_entrata(i))
    print()
    print(f"tempo totale: {tempo_totale(z)} minuti")
    print()

    print('tempo per categoria:')
    for categoria, tempo in tempo_per_categoria(z).items():
        print(f"- {categoria}: {tempo} minuti")
    print()
    
    salva_diario(z, "diario.json")
    print()

    print('Diario caricato:')
    for i in carica_diario("diario.json")['entrate']:
        print(info_entrata(i))


if __name__ == "__main__":
    main()