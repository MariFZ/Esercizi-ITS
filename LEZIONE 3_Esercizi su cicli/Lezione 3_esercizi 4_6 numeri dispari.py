# 4.6 Numeri dispari:
# 1. Usate il terzo argomento della funzione range() per creare una lista dei numeri dispari da 1 a 20. 
# 2. Utilizzate un ciclo for per stampare ogni numero.

# Lista per numeri dispari di 1 a 20

number: list[int] = list(range(1,21))

for number in range(1,20,2):
   print(f"Questa è la lista di numeri dispari tra 1 e 20: {number}")
                                                           
# stampa senza usare una lista, solo usando la funzione range


# for number_dispari in range(1,20,2):
#    print(f"Questa è la lista di numeri dispari tra 1 e 20: \n{number_dispari}")