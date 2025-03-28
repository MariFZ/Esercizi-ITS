# Esercizio 5

# Scrivere una funzione add_one(). Prende come argomento un numero intero. La funzione aggiunge 1 al numero intero e lo restituisce. 
# Scrivere un'altra funzione add_one_to_list(). 
# Definite una variabile new_list in questa funzione. Utilizzando un ciclo for, iterate attraverso l'elenco degli argomenti. 
# Utilizzando add_one(), riempite new_list con i numeri interi dell'elenco di argomenti incrementati di 1. Stampate new_list.
# Esempio:add_one_to_list([1, 2, 3])>>> [2, 3, 4]

def add_one(numero: int) -> int: 

    return numero + 1       # Restituisce il numero incrementato di 1

x = add_one(5)
print(x)
 
 
def add_one_to_list(lista_numeri: list[int]):
    
    new_list: list[int] = []
    
    for number in lista_numeri:
        
        new_list.append(add_one(number)) 

    print(f"{new_list}")


lista_incrementata = add_one_to_list([2,4,6])

# print(lista_incrementata)


