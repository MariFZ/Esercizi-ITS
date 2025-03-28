# ESERCIZIO # 2

# Trova il massimo tra 4 numeri: Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.

massimo = 0
contatore = 0

while contatore < 4:
    n = int(input("Scrive un numero: "))
    if n > massimo:
        massimo = n
    contatore += 1
        
else:
    print(f"Il numero massimo dei 4 numeri che hai inserito è: {massimo} ")

