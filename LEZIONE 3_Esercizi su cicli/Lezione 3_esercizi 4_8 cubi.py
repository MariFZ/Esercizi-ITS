# 4-8. Cubi:
# Un numero elevato alla terza potenza si chiama cubo: Ad esempio, il cubo di 2 si scrive 2**3 in Python. 
# 1. Creare una lista dei primi 10 cubi (cioè il cubo di ogni numero intero da 1 a 10) e utilizzare un ciclo for per stampare il valore di ogni cubo.

cubo: list[int] = list(range(1,11))

for number in cubo:
    print(f"Questo è il valore di ogni cubo dei numeri interi tra 1 e 10: {number**3}")

