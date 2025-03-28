# ESERCIZIO 1 DISPENSA

# Scrivete una funzione check_value(), che prenda un numero come argomento. 
# Usando if/ else, la funzione deve stampare se il numero è più grande, più piccolo o uguale a 5.


def check_value(a:int) -> int:

    if a > 5:
        print(f"Il numero {a} è maggiore di 5")
    elif a < 5:
        print(f"Il numero {a} è minore di 5")
    else: 
        print(f"Il numero {a} è uguale a 5")
    
    # return a NON DEVO FARE IL RETURN

check_value(10)

# print(f"Questo è il numero che ho inserito: {numero}")


