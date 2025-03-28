# ESERCIZIO 8


# Scrivi una funzione che prende una lista di numeri 
# e restituisce la media dei numeri.

def media_numeri(lista: list[int]) -> list[int]:

    somma = 0
    media = 1

    for numero in lista:
        somma += numero
        media = somma/len(lista)

    return media

numeri: list[int] = [2,3,4,56,7,8,9]

print(f"Questa è la media dei nuemri che hai inserito: {media_numeri(numeri):.2f}")
