# ESERCIZIO 8.10
# Sending Messages: 

# Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message 
# and moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly

# Iniziare con una copia del programma dell'Esercizio 8-9. 
# Scrivete una funzione chiamata send_messages() che stampa ogni messaggio di testo e sposta ogni messaggio in un nuovo elenco chiamato 
# sent_messages man mano che viene stampato. 
# Dopo aver richiamato la funzione, stampate entrambi gli elenchi per verificare che i messaggi siano stati spostati correttamente.




lista1: list = ["Ciao Roma!", "Cosa mangiamo?", "Domani piove"]

def send_message(lista) -> list[str]:

    # Stampo un messaggio generico 
    print(f"Questi sono i messaggi presenti in lista: {lista}")

    # creo la nuova lista che riceve i messaggi

    sent_message: list[str] = []

    # Creo il ciclo for che prende i messagi da lista e gli metti nell'altra lista
    # creo una variabile contatore per sommare le iterazioni con base alla lunguezza della lista

    contatore = 0

    if contatore < len(lista):

        for text in lista:
            sent_message.append(text)
            contatore += 1
            print(f"Il testo {text} è stato aggiunto")

    print(f"Questa è la lista originale: {lista} e questa è la seconda lista: {sent_message}")

send_message(lista1)

# Seconda possibilità con for in range


# def send_messages(lista) -> list[str]:

#         sent_messages: list = []

#         lunguezza = len(lista)
#         print(f"{lista=}\n{send_messages=}\n\n")

#         for i in range (lunguezza): 
#             message = lista.pop(0)
#             sent_messages.append(message)

#             print(f"{lista=}\n{sent_messages=}\n\n")
            
# send_messages(lista1)





































# Grandi maghi
# Iniziate con una copia del vostro programma dall'Esercizio 8-9. 
# Scrivete una funzione chiamata make_great() che modifichi l'elenco dei maghi aggiungendo la frase the Great al nome di ogni mago. 
# Chiamate show_magicians() per vedere che l'elenco è stato effettivamente modificato.



# def show_magicians(magicians):
#     """Print the name of each magician in the list."""
#     for magician in magicians:
#         print(magician)

# def make_great(magicians):
#     """Add 'the Great!' to each magician's name."""
#     # Build a new list to hold the great musicians.
#     great_magicians = []

#     # Make each magician great, and add it to great_magicians.
#     while magicians:
#         magician = magicians.pop()
#         great_magician = magician + ' the Great'
#         great_magicians.append(great_magician)

#     # Add the great magicians back into magicians.
#     for great_magician in great_magicians:
#         magicians.append(great_magician)

# magicians = ['Harry Houdini', 'David Blaine', 'Teller']
# show_magicians(magicians)

# print("\n")
# make_great(magicians)
# show_magicians(magicians)