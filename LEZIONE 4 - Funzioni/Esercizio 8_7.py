# ESERCIZIO 8.6

# Album: 

# Scrivere una funzione chiamata make_album() che costruisca un dizionario che descriva un album musicale. 
# La funzione deve ricevere il nome dell'artista e il titolo dell'album e deve restituire un dizionario contenente queste due informazioni. 
# Usate la funzione per creare tre dizionari che rappresentano album diversi. 
# Stampate ogni valore restituito per dimostrare che i dizionari memorizzano correttamente le informazioni sugli album. 
# Utilizzare None per aggiungere un parametro opzionale a make_album(), che consente di memorizzare il numero di brani di un album. 
# Se la riga di chiamata include un valore per il numero di canzoni, aggiungerlo al dizionario dell'album. 
# Eseguire almeno una nuova chiamata di funzione che includa il numero di canzoni di un album.


# Prima versione con nome e titolo

def make_album(nome_artista, titolo_album) -> dict[str]:
    
    album_musicale: dict[str] = {'nome': nome_artista, 'titolo': titolo_album }

    return (album_musicale)



artista1 = make_album("Dido", "Yesterday")

artista2 = make_album("Ludovico", "Domani")

print(artista1)

print(artista2)

# Seconda versione, creando un valore di default su brani

def make_album(nome_artista, titolo_album, brani= None) -> dict[str, str, int]:
    
    album: dict[str,str,int] = {"nome": nome_artista, "titolo": titolo_album}

    if brani != None:
        album["Numero_canzoni"]= brani

    return album


artista3 = make_album("MJ", "Tomorrow", 34)

print(artista3)

artista4 = make_album("Sting","In New York")


print(artista4)




# def make_album(nome_artista:str, nome_album: str, numero_canzoni: int = None) -> dict[str,str, int]:    # In questa parte devo scrivere i valori che saranno inseriti

#     album: dict = {"Nome": nome_artista, "Album": nome_album, "Canzoni": numero_canzoni}                # qui le chiavi scritte in virgolette

#     return album


# artista1 = make_album("Mickey Jackson","Imagine")

# artista2 = make_album("Shakira", "Ayer")

# artista3 = make_album("Mickey Jackson","Imagine", 23)

# print(f"Questo è l'album di del primo artista: {artista1}")

# print(f"Questo è l'album del secondo {artista2}")

# print(f"Questo è l'album del terzo {artista3}")









