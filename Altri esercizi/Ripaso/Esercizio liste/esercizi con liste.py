# Esercizi con liste 

# esercizio 2 - quiz 4 aprile

# Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, dove n è la lunghezza della lista. 
# Tuttavia, alcuni numeri potrebbero mancare: la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.

# Il tuo compito è individuare i numeri mancanti.

# Scrivi una funzione che, data in input una lista, 
# restituisca una nuova lista ordinata contenente tutti i numeri da 1 a n che non sono presenti nella lista originale.

'''in altre parole: dovevo fare una lista lunga solo quanto la lunguenza:
cioè: se la lunguezza era da 5, numeri da 1 a 5 e vedere quali numeri erano già presenti nella lista data
se la lunguenza è 10, vedere quali numeri nella lista data, erano già presenti: numeri da 1 a...10 
'''

# def find_disappeared_numbers(nums:list[int]) -> list[int]:

#     numeri_mancanti = []

#     for i in range(1, len(nums) +1):

#         if i not in nums:
#             numeri_mancanti.append(i)

#     return numeri_mancanti

#print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))

# print(find_disappeared_numbers([1,8,9,150]))

# esercizio 3

# Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
# La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.

# def somma_elementi(x: list[int], y: list[int]) -> list[int]:

#     n = len(x)

#     new_list = []
#     somma = 0

#     for i in range(n):
#         somma = x[i] + y[i]
#         new_list.append(somma)

#     return new_list

# print(somma_elementi([-18,2,4,5,1,10,12,45,-1,0,45,0,0,0],[-18,92,91,0,12,-1,48,53,0,0,0,0,-1,7]))

# ESERCIZIO 5
# esercitazione code 5

# Scrivi una funzione che prende una lista di parole 
# e restituisce una lista contenente la lunghezza di ciascuna parola.

# def lenparole(lista: list[str]) -> list[str]:

#     len_parole:list = {}

#     for parola in lista:
#         # len_parole.append(len(parola))
#         len_parole[parola] = len(parola)

#     return len_parole

# esercizio 2
# primo quiz


# Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.


def remove_duplicates(lista: list[str, int]) -> list[str, int]:

    new_list:list = []
    da_ordinare = lista.copy()

    for elem in lista:
        if elem not in new_list:
            new_list.append(elem)

    return new_list

print(remove_duplicates([1, 2, 3, 1, 2, 4]))
# print(remove_duplicates([4, 5, 'a', 4, 6]))
# print(remove_duplicates(['a', 'b', 'a']))
# print(remove_duplicates([1, 1, 1, 1]))

# esercizio 5
# primo quiz

# Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista

# def frequency_dict(elements: list) -> dict:

#     dizionario = {}

#     for ele in elements:
#         if ele not in dizionario:
#             dizionario[ele] = 1
        
#         else:
#             dizionario[ele] +=1

#         # elif ele in dizionario:
#         #     dizionario[ele] += 1

#     return dizionario

# # print(frequency_dict(['mela', 'banana', 'mela']))
# print(frequency_dict([1, 2, 2, 3, 3, 3]))

# esercizio 7
# quiz

# Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
# cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
# For example

# print(check_parentheses("()()"))
# True
# print(check_parentheses("(()))("))
# False

def check_parentheses(expression: str) -> bool:

    check = []
    aperte = "("
    chiuse = ")"

    for p in expression:
        if p == aperte:
            check.append(p)
        elif p == chiuse:
            if len(check) != 0:
                return False
            check.pop()

    return len(check) == 0

print(check_parentheses("(()))("))










