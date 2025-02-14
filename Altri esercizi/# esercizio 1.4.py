# esercizio 1.4
"""Si scriva un programma che dato un intero di quattro cifre, per esempio 2024, utilizzando gli opportuni operatori, lo si visualizzi, una cifra per riga"""

intero: int = 2025
for numero in str(intero): 
    print(numero)

# seconda possibilità più confusa: 
intero: int = 2025
stringa: str =str(intero)
for numero in stringa:
        print(numero)



