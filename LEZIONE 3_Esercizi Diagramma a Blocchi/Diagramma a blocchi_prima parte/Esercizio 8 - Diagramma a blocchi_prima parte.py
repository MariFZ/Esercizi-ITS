# ESERCIZIO 8

# Trovare i numeri maggiori di un valore soglia. 

# Progetta un algoritmo che dati 7 numeri, trova e comunica 
# i numeri maggiori di un valore soglia fornito dall'utente.

i = 0
num_soglia = 0

soglia = int(input("Inserisci il numero soglia: "))

while i < 7:
    numero = int(input("Inserisci un numero: "))
    if numero > soglia:
        num_soglia += 1
    i += 1

print(f"La soglia dei numeri che hai inserito è: {num_soglia}")