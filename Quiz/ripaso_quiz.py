# ripaso quiz

# Primo esercizio
# Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.

# SOLUZIONE PIU INTELLIGENTE
# def list_statistics(numbers: list[int]) -> list[int] :

#     massimo = max(numbers)
#     minimo = min(numbers)
#     somma = sum(numbers)

#     return massimo, minimo, somma/len(numbers)

# SOLUZIONE MOLTO LUNGA MA COMUNQUE VALIDA

def list_statistics(numbers: list[int]) -> list[int] :

    # qui sto prendendo il primo numero della lista all'indice 0 e faccio il confronto con gli altri
    massimo:int = numbers[0]
    minimo:int = numbers[0]
    somma:int = 0


    for n in numbers:
        if n > massimo:
            massimo = n
        elif n < minimo:
            minimo = n
        somma += n
    
    return massimo, minimo, somma/len(numbers)


# lista1 = [1, 2, 3, 4, 5]
# print(list_statistics(lista1))

# lista2 = [10, 20, 30, 40, 50]
# print(list_statistics(lista2))

# lista3 = [-5, -1, -3]
# print(list_statistics(lista3))

# Esercizio 2

# Scrivi una funzione che rimuove tutti i duplicati da una lista, 
# contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi

# def remove_duplicates(lista: list[str, int]) -> list[str, int]:

#     new_lista:list = []

#     for elemento in lista:
#         if elemento not in new_lista:
#             new_lista.append(elemento)
    
#     return new_lista


# lista4:list = [1, 2, 3, 1, 2, 4]
# print(remove_duplicates(lista4))

# Esercizio 3

# Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.

# def countdown(n: int) -> int:

# # col ciclo while
#     i = -1
#     while i < n:
#         i += 1
#         print(i)

# countdown(5)

# col ciclo for
# def countdown(n: int) -> int:

#     rovescia:list = []

#     for number in range(n+2-1):
#        rovescia.append(number)
#        print(number)

#     return rovescia
   
# def countdown(n: int):

#     while n >= 0:
#         print(n)
#         n -= 1  # Decrementa il valore di n



# (countdown(5))
    

# esercizio 4

# La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
# Un errore nell'implementazione porta a risultati inaspettati.
# Trova l'errore e correggi il codice affinché soddisfi i casi di test.
# For example:

# def calculate_average(numbers: list[int]) -> float:
#     if len(numbers) == 0:
#         return sum(numbers) / len(numbers)
#     else:
#         return len(numbers) / sum(numbers) – 1




def calculate_average(numbers: list[int]) -> float:
    

    if len(numbers) == 0:
        '''se la lista è vuota...stampa zero'''
        return 0 
    else:
        return sum(numbers)/len(numbers) # '''dovevo invertire la posizione'''


# lista5 = [1, 2, 3, 4, 5]
# print(calculate_average(lista5))

# lista6 = []
# print(calculate_average(lista6))

# lista7 = [10, 20, 30]
# print(calculate_average(lista7))

# esercizio 5

# Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

# def frequency_dict(elements: list) -> dict:

#     dizionario:dict = {}

#     for elemento in elements:
#         if elemento not in dizionario:
#             dizionario[elemento] = 1
#         elif elemento in dizionario:
#             dizionario[elemento] += 1

#     return dizionario

# lista8:list = ['mela', 'banana', 'mela']
# print(frequency_dict(['mela', 'banana', 'mela']))       

# esercizio 6

# Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.

# def rounded_average(numbers: list[int]) -> int:

#     media = sum(numbers)/len(numbers)

#     return round(media)

# lista9:list = [1, 1, 2, 2]

# print(rounded_average(lista9))

# esercizio 7
# Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente
# parentesi che chiude.

# def check_parentheses(expression: str) -> bool:

#     bilanciata:list = []

#     for p in expression:
#         if p == "(":
#             bilanciata.append(p)

#         elif p == ")":
#             if not bilanciata: # se la lista non è vuota
#                 return False
#             bilanciata.pop() # se la lista non è vuota, elimina l'ultima parentesi aperta


#     return len(bilanciata) == 0 


# stringa1 = ("()()")
# print(check_parentheses(stringa1))

# stringa2 = "(()))("
# print(check_parentheses(stringa2))

# esercizio 8

# Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
# ritorni un nuovo insieme senza i numeri specificati nella lista

# def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:

#     set_new:set = set() 

#     for elemento in original_set:
#         if elemento not in elements_to_remove:
#             set_new.add(elemento)
    
#     return set_new

# set1 = {5, 6, 7}
# lista10 = [7, 8, 9]

# print(remove_elements(set1, lista10)) 

# esercizio 10

# Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:

    new_dizionario:dict = dict1.copy()

    for item, valore in dict2.items():
        if item in new_dizionario:
            new_dizionario[item] += valore
        else:
            new_dizionario[item] = valore

    return new_dizionario


# print(merge_dictionaries({'x': 5}, {'x': -5}))

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
            