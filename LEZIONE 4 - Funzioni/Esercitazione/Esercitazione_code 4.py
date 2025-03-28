# ESERCIZIO 4

# Scrivi una funzione che prende una lista di numeri 
# e restituisce una lista contenente solo i numeri pari.

def numeri_pari(lista: list[int]) -> list[int]:

    lista_pari: list[int] = []

    for numero in lista:
        if numero % 2==0:
            lista_pari.append(numero)

    return lista_pari

lista_numeri: list[int] = [2,3,4,5,6,7,8,9,10]

print(f"Questa è la lista dei numeri pari della lista: {numeri_pari(lista_numeri)}")
    
