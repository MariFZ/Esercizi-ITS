#ESERCICIO 1. 

# Imagine you're participating in aMario Kartrace with your friends. Each player finishes the race in a specific position.
# Write a Python program that takes as input the finishing position of a player, given as a positive integer, and returns the position in cardinal form
# (e.g.,"1st","2nd","3rd","4th","5th",etc.).

# ExpectedOutput:
# Finishingposition:1
# 1st!
# --------------------------
# Finishingposition:2
# 2nd!
# ---------------------------
# Finishingposition:4
# 4th!
# ----------------------------


number: int = int(input("Inserisci la posizione finale: ")) 
# la funzione int() accetta solo stringhe che rappresentano numeri interi (come "8", "42", "-3"), non numeri decimali.

match number:

    case 1: 
        print(f"{number}st!")
    
    case 2: 
        print(f"{number}nd!")
    
    case 3: 
        print(f"{number}rd!")
    
    case 4: 
        print(f"{number}th!")

    case _:
        print(f"{number}th!")


    


