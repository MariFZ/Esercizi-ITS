# ESERCIZIO 8-8
# Album utente
# Iniziare con il programma dell'Esercizio 8-7. Scrivere un ciclo while che consenta agli utenti di inserire l'artista e il titolo di un album. 
# Una volta ottenute queste informazioni, chiamare make_album() con l'input dell'utente e stampare il dizionario creato. 
# Assicurarsi di includere un valore di quit nel ciclo while.

def make_album(nome_artista:str, titolo_album: str) -> dict[str,str]:  

    album: dict = {"Nome": nome_artista, "Titolo": titolo_album}

    return album

# Creo un ciclo while True
while True:

    # Chiedo l'opzione di inserire o no i dati dell'artista, con la risposta "no" chiudo il ciclo
    opzione: str = input("Vuoi inserire il nome di un artista e il suo album? (si/no): ")

    # Se l'opzione è "yes" entro nel ciclo
    if opzione == "si":

    # Creo le due variabili che mi servono per inserire nella funzione

        nome_artista: str = (input(f"Scrive il nome dell'artista: "))
        titolo_album: str = (input("Scrive il titolo dell'album: "))
       
    # Stampo l'informazione dell'artista avuta in input
        print(make_album(nome_artista, titolo_album))

    # Con questa opzione esco dal ciclo
    elif opzione == "no":
        break

print("Grazie dell'informazione!")











