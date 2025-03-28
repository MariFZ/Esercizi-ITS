# ESERCIZIO 8.11

# Maghi immutati
# Iniziate con il vostro lavoro dall'Esercizio 8-10. Chiamate la funzione make_great() con una copia dell'elenco dei nomi dei maghi. 
# Poiché l'elenco originale rimarrà invariato, restituite il nuovo elenco e memorizzatelo in un elenco separato. 
# Chiamate show_magicians() con ogni lista per mostrare che avete una lista di nomi originali e una lista con il Grande aggiunto al nome di ogni mago.

# 8-11. Archived Messages: 
# Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.

# 8-11. Messaggi archiviati: 
# Iniziare con il lavoro svolto nell'Esercizio 8-10. Chiamate la funzione send_messages() con una copia dell'elenco dei messaggi. 
# Dopo aver richiamato la funzione, stampate entrambi gli elenchi per mostrare che l'elenco originale ha conservato i suoi messaggi.

lista1: list = ["Ciao Roma!", "Cosa mangiamo?", "Domani piove"]


def send_messages(lista: list):

        sent_messages: list = []

        for texto in lista: 
            sent_messages.append(texto)

        print(f"{lista=}\n{sent_messages=}\n")
            
send_messages(lista1)

























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

#     return magicians

# magicians = ['Harry Houdini', 'David Blaine', 'Teller']
# show_magicians(magicians)

# print("\nGreat magicians:")
# great_magicians = make_great(magicians[:])
# show_magicians(great_magicians)

# print("\nOriginal magicians:")
# show_magicians(magicians)