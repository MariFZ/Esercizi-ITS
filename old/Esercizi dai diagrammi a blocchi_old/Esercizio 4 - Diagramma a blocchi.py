# ESERCIZIO 4

# Controllo della parità di un numero. 
# Progetta un algoritmo utile a determinare se un numero inserito dall'utente è pari o dispari.

pari = 0
dispari = 0

numero = int(input("Inserisci un numero: "))

if numero % 2 == 0:
    print("Il numero è pari")
else: 
    print("Il numero è dispari ")