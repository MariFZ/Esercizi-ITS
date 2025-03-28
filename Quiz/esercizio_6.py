# esercizio 6

# Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.


def rounded_average(numbers: list[int]) -> int:
    '''Il metodo più veloce usando le funzioni'''

    
    media = sum(numbers)/len(numbers)
    print(media)

    return round(media)

print(rounded_average([1, 2, 3, 4, 5]))

def rounded_average(numbers: list[int]) -> int:
    '''Metodo più artiginale ;)...cioè meno esperto :)'''

    somma = 0
    media = 0

    for numero in numbers:
        somma += numero
        media = somma/len(numbers)
    
    return round(media)


print(rounded_average([1, 1, 2, 2]))


