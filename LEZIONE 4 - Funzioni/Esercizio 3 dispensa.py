# ESERCIZIO 3 DISPENSA

# Scrivete una funzione print_numbers(), che prende come argomento un elenco di numeri. 
# Utilizzando un ciclo for, stampate ogni numero uno per uno.

def print_numbers(numeri:list) -> list[int]:

    for i in numeri:
        print(i)

list1: list[int] = [2,4,6,8,10]
list2: list[int] = [10,20,30,40,50]

print_numbers(list1)
print_numbers(list2)