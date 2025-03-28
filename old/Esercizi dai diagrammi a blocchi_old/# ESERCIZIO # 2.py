# ESERCIZIO # 2

# Trova il massimo tra 4 numeri: Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.

massimo = 0
contatore = 1

while contatore <= 4:
    n = input(input("Scrive un numero: "))
    if (n > massimo):
        massimo = n
    contatore += 1
else:
    print("massimo")

# esercizio 3. Progettare un algoritmo che calcoli la somma dei soli numeri positivi tra 5 valori inseriti dall'utente. Quindi, se un numero è negativo o zero, ignora quel valore nella somma.

sum = 0
cont = 1

A = int(input("Inserire A: ")) # Read A
B = int(input("Inserire B: ")) # Read B
