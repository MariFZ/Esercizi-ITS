# ESERCIZIO 6

# Progetta un algoritmo per calcolare il fattoriale di un numero intero positivo fornito dall'utente.

number = int(input("Inserisci un numero: "))

if number > 0:
    
    i = 1
    fatt = 1
    while i <= number: 
        fatt = fatt * i
        i += 1
    print(f"Il numero fattoriale di {number} è: {fatt}")
else:
    print("Il numero inserito deve essere positivo") 
    
    
    

    
    
        

        