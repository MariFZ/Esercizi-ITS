sum:int = 0

articolo1: float = 10.50
articolo2: float = 7.50
articolo3: float = 5.00

# sum = articolo1 + articolo2 + articolo3

# primo prodotto: SAREBBE LA SOMMA DI 0 + 10.5 (SUM AVEVA IL VALORE 0)
sum = sum + articolo1
print(sum)

# articolo articolo2 ---- QUI PERCHE HO CAMBIATO LA VARIABILE SUM CHE ADESSO HA IL VALORE 10,5
sum = sum + articolo2
print(sum)

#articolo 3
sum += articolo3 # sum = sum + articolo3
print(sum)

sum *=2 # sum = sum *articolo2
print(sum)

sum /= 3 # sum = sum /3
print(sum)

sum /= 3 # sum = sum /3
print(int(sum)) # qui ho chiesto di darmi il numero intero con la scritta int



