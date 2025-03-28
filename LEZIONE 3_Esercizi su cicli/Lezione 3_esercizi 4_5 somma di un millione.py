# 4-5. Somma di un milione:
# 1. Fate una lista di numeri da uno a un milione e poi usate min() e max() per assicurarvi che la lista inizi effettivamente con 1 e finisca con un 1000000. 
# 2. Usate anche la funzione sum() per vedere quanto velocemente Python può sommare un milione di numeri.

numbers: list[int] = list(range(1, 1000001))

# Verifica che la lista inizi con 1 usando min()

print(min(numbers))

# Verifica che la lista inizi con 1 usando max() !! 

print(max(numbers))

# funzione sum

print(f"Questo è il risultato della somma dei numeri da 1 a 1000000: \n {(sum(numbers))}")