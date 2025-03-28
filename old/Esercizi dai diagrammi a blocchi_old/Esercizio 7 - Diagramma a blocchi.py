# ESERCIZIO N.7

# Conta i numeri pari e dispari. 
# Progetta un algoritmo che dati 10 numeri forniti dall'utente, conta quanti sono pari e quanti dispari.

pari = 0
dispari = 0
cont = 0

while cont <= 10:
    number = int(input("Inserisci un numero: "))
    if number % 2 ==0:
        pari += 1
    dispari += 1
    cont += 1
else:
    print(f"I numeri pari sono: {pari}")
    print(f"I numeri dispari sono {dispari}")