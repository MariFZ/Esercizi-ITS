# ESERCIZIO 10

# Scrivi una funzione che prende una lista di numeri 
# e restituisce una lista contenente solo i numeri maggiori di un valore specificato.

def maggiori_di(lista: list[int], maggiore: int) -> tuple[list[int], int]:


    maggiori: list[int] = []

    for numero in lista:
        if numero > maggiore:
            maggiori.append(numero)
    
    return maggiori

lista_numeri: list[int] = [10,34,5,6,78,12,33,4,1]
numero_maggiore: int = 34

print(maggiori_di(lista_numeri,numero_maggiore))

# print(f"Questa è la lista dei numeri maggiori di {numero_maggiore} della lista fornita: {maggiori_di(lista_numeri, numero_maggiore)}")


