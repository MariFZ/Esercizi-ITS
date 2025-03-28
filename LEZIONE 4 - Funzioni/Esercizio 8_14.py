# ESERCIZIO 8.14

# Cars
# Write a function that stores information about a car in a dictionary. the function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, 
# such as a color or an optional feature. Your function should work for a call like this one:

# car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary that’s returned to make sure all the information was stored correctly.

# Scrivete una funzione che memorizzi le informazioni su un'automobile in un dizionario. La funzione deve sempre ricevere il nome del produttore e del modello. 
# Deve poi accettare un numero arbitrario di argomenti di parole chiave. Chiamate la funzione con le informazioni richieste e altre due coppie nome-valore, come un colore o una caratteristica opzionale. 
# La funzione dovrebbe funzionare per una chiamata come questa: 
# car = make_car('subaru', 'outback', color='blue', tow_package=True) 
# Stampare il dizionario che viene restituito per assicurarsi che tutte le informazioni siano state memorizzate correttamente.

def makecar(nome_produttore, modello, **informazioni):

    # creo il dizionario con i dati obbligatori: nome del produttore e modello

    macchina = {'produttore': nome_produttore, 'model_car': modello,}

    '''con i dati che provengono da: informazioni, creo un ciclo for, 
        che aggiungerà sia la chiave e il valore al dizionario, 
        uso il metodo .items() che mi da, sia la chiave e il valore'''

    for chiave, valore in informazioni.items():
        macchina[chiave] = valore
        
    return macchina

macchina1 = makecar('Toyota', 'Corolla', color='grigio', autoradio=True)

print(macchina1)


if __name__== "__main__":











































































# def make_car(manufacturer, model, **options):
#     """Make a dictionary representing a car."""
#     car_dict = {'manufacturer': manufacturer.title(),'model': model.title(),}
#     for option, value in options.items():
#         car_dict[option] = value

#     return car_dict

# my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(my_outback)

# my_accord = make_car('honda', 'accord', year=1991, color='white', headlights='popup')
# print(my_accord)