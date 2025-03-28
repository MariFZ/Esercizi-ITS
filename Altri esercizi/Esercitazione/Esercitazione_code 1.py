# ESERCIZIO 1
# FUNZIONE SOMMA DI NUMERI IN UNA LISTA
# Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi


def somma_numeri(lista_numeri: list) -> list[int]: # definisco la funzione che prenderà i valori di una lista

    somma: int = 0              # inializzo la variabile che sommerà i numeri

    for number in lista_numeri: # inizio il ciclo for che prenderà ogni elemento della lista
        somma += number         # aggiorno la somma + il numero iterato

    return somma                # ritono il valore perchè possa essere usato

                 
# Creo le liste che contengono i numeri
pari: list[int] = [2,4,6,8]    
dispari: list[int] = [1,3,5,7]


# Per stampare il risultato della somma, ho due possibilita:

# 1) Inserisco il valore dentro di una variabile

risultato: tuple[int] = somma_numeri(pari)
print(risultato)

# 2) Chiamo la funzione dentro il print

print(f"Questa è la somma dei numeri pari: {somma_numeri(pari)} e la dei numeri dispari: {somma_numeri(dispari)}")

# --------------------------------------------------------------------------------
# SOTTO CI SONO ALTRI ESERCIZI


# def somma_lista(lista): 

#     somma:int = 0

#     for i in lista:
#         somma += i
#     return somma

# numeri: list[int] = [1,2,3,4]

# number: list[int] = [10,20,30]

# # risultatoa = somma_lista(numeri)

# # risultatob = somma_lista(number)

# # print(risultatoa)
# # print(risultatob)

# print(type(somma_lista(numeri)))

# print(type(somma_lista(number)))


