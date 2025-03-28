# ESERCIZIO 6

# Scrivi una funzione che prende una lista di numeri e restituisce il valore massimo


# # Funzione con il metodo max()
# def numeromax(lista: list[int]) -> list[int]:

#     lista: list[int] = max(lista)

#     return lista


# lista_numeri: list[int] = [23,56,78,34,90,23,456]

# print(f"Questo è il numero più alto della lista: {numeromax(lista_numeri)}")

# Funzione con il ciclo for

def numeromax(lista: list[int]) -> list[int]:

    maximo: list[int] = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
    
    return maximo

lista_numeri: list[int] = [23,56,45678,34,90,23]

print(f"Questo è il numero più alto della lista: {numeromax(lista_numeri)}")

print(type(numeromax(lista_numeri)))