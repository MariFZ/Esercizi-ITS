# Esercizio 3C-00A. Scrivere un programma in Python che richieda all'utente di inserire un numero intero rappresentante 
# il numero di neonati e utilizzi lo statement match per fornire una risposta appropriata:

# - Se il numero inserito è 1, stampare "Congratulazioni!"
# - Se il numero inserito è 2, stampare "Wow! Gemelli!"
# - Se il numero inserito è 3, stampare "Wow! Tre!"
# - Se il numero inserito è 4, stampare "Mamma mia Quattro! Wow!"
# - Se il numero inserito è 5, stampare "Incredibile! Cinque!"
# - Altrimenti, stampare "Non ci credo! n bambini!", sostituendo n con il numero inserito.


numero: int = int(input("Inserire il numero di neonati: "))

match numero:


    case 1:
        print(f"{numero} \"Congratulazioni!\"")
    
    case 2:
        print(f"{numero} \"Wow! Gemelli!\"")

    case 3:
        print(f"{numero} \"Wow! Tre!\"")
        
    case 4:
        print(f"{numero} \"Mamma mia Quattro! Wow!\"")
        
    case 5:
        print(f"{numero} \"Incredibile! Cinque!\"")
        
    case _:
        print(f"\"Non ci credo! {numero} bambini!\"")
    
