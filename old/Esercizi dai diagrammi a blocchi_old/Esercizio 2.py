# ESERCIZIO 5

numero = int(input("Inserisci un numero: "))
if numero < 2:
    print("Il numero non è primo")
else:
    div = 2
while div < numero:
    numero % div == 0
    div += 1
print("Il numero è primo")

# 6. Calcolo del fattoriale di un numero

def calcola_fattoriale(n):
    fattoriale = 1
    for i in range(1, n + 1):  # Ciclo da 1 a n
        fattoriale *= i  # Moltiplica fattoriale per i
    return fattoriale

# Input dall'utente
try:
    numero = int(input("Inserisci un numero intero positivo: "))
    if numero < 0:
        print("Errore: il numero deve essere positivo.")
    else:
        risultato = calcola_fattoriale(numero)
        print(f"Il fattoriale di {numero} è: {risultato}")
except ValueError:
    print("Per favore inserisci un numero intero valido.")

 