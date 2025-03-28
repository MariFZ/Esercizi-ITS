# Esercizio 3. Calcolo della somma di numeri positivi

# Progettare un algoritmo che calcoli la somma dei soli numeri positivi tra 5 valori inseriti dall'utente. 
# Quindi, se un numero è negativo o zero, ignora quel valore nella somma.

somma = 0
cont = 1


while cont <=5:
    n = int(input("Inserire un numero: "))
    if n > 0:
        somma += n
    cont += 1

print(f"La sommma dei numeri che hai inserito è: {somma}")


