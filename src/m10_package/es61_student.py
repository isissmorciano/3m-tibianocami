from musica.playlist import (
    
    crea_playlist,
    aggiungi_canzone,
    mostra_playlist
)
from musica.canzoni import crea_canzone

def main( ):



    playlist = crea_playlist("Le mie canzoni preferite")


    c1 = crea_canzone("Bohemian Rhapsody", "Queen", 355)
    c2 = crea_canzone("Stairway to Heaven", "Led Zeppelin", 482)
    c3 = crea_canzone("Hotel California", "Eagles", 390)


    aggiungi_canzone(playlist, c1)
    aggiungi_canzone(playlist, c2)
    aggiungi_canzone(playlist, c3)


    print(mostra_playlist(playlist))




if __name__ == "__main__":
    main()