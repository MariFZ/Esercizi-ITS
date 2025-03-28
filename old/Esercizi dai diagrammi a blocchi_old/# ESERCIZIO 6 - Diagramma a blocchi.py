# ESERCIZIO 6

# Progetta un algoritmo per calcolare il fattoriale di un numero intero positivo fornito dall'utente.

number = int(input("Inserisci un numero: "))

if number <= 0:
    print("Il numero inserito deve essere positivo")
else:
    i = 1
    fatt = 1
    if i <= number:
        fatt = fatt * i
        i = i +1 
    print(f"Il fattoriale di {number} è {fatt}: ")
        

        