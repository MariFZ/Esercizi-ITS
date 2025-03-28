# 4-7. Tre:
# 1. Fare una lista dei multipli di 3, da 3 a 30. 
# 2. Utilizzate un ciclo for per stampare i numeri dell'elenco.

numbers: list[int] = list(range(1,31))

for numbers in range(3,30,3):
    print(f"Questi sono i numeri multipli di 3 tra 3 e 30: \n {numbers}")


# numbers: list[int] = list(range(3,30,3))
