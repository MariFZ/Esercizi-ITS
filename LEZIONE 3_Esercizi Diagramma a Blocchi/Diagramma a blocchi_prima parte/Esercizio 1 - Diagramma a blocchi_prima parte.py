# ESERCIZIO n.1
# Calcolo cateto di un triangolo rettangolo:

# Progetta un algoritmo per ottenere la misura di un cateto c in un triangolo rettangolo, 
# conoscendo quelle dell’ipotenusa a e dell’altro cateto b

import math

a = int(30)
b = int(20)

if a > b:
    c: float = math.sqrt((a*a)-(b*b))
    print(f"Il valore del cateto c è: {c}")
else: 
    print("Errore. il valore di a debe essere minore di b")

