# esercizio 5

# Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.


def frequency_dict(elements: list) -> dict:

    numeri_elementi = {}
    
    for elemento in elements:

        if elemento not in numeri_elementi:
            numeri_elementi[elemento] = 1

        elif elemento in numeri_elementi:
            numeri_elementi[elemento] += 1
        
        '''Nel test ho sbagliato qui:
        numeri_elementi[elemento] = 1 + 1 
        Facendo così ho sommato solo 2 volte

        Invece scrivendo:
        numeri_elementi[elemento] += 1
        salvo il valore ottenuto e alla prossima iterazione, 
        sommo il prossimo numero
         
         '''
        
    return numeri_elementi

print(frequency_dict(['mela', 'banana', 'mela']))
print(frequency_dict([1, 2, 2, 3, 3, 3]))









