# esercizio 5

# Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:

# tutti i numeri pari vengano prima di tutti i numeri dispari;

# l’ordine relativo tra pari e dispari va mantenuto;

# l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.

def even_odd_pattern(numbers:list[int]) -> list[int]:

    list_ordinata:list = []

    pari:list = []
    dispari:list = []

    for number in numbers:
        if number %2 ==0:
            pari.append(number)
        else:
            dispari.append(number)

    
    list_ordinata = pari + dispari # cosi sommo le lsite

    

    
    return pari.extend(dispari)

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))

