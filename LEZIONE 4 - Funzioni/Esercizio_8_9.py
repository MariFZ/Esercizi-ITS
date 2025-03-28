# ESERCIZIO 8.9

# Messaggi:
# Creare un elenco contenente una serie di brevi messaggi di testo. 
# Passare l'elenco a una funzione chiamata show_messages(), che stampa ogni messaggio di testo

# Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message


def show_messages(lista: str) -> list[str]:
    
    # stampo un messaggio generico
    print(f"Questi sono i messaggi dentro della lista: \n")

    # inizio il ciclo for, in ognuno stampo ogni piccola frase presente nella lista
    for text in lista:
      print(text)
    
    
lista1: list = ["Ciao Roma!", "Cosa mangiamo?", "Domani piove"]

show_messages(lista1)










































# def show_magicians(magicians):
#     """Print the name of each magician in the list."""
#     for magician in magicians:
#         print(magician.title())

# magicians = ['harry houdini', 'david blaine', 'teller']
# show_magicians(magicians)