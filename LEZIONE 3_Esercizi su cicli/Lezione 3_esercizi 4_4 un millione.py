# 4-4. Un milione:
# Creare una lista di numeri da uno a un milione e poi utilizzare un ciclo for per stampare i numeri. 
# Se l'output richiede troppo tempo, interromperlo premendo CTRL-C o chiudendo la finestra di output

# lista

lista = list(range(1,1000001))

# for i in range(1, 1000001):
#     print(i)

for i in lista:
    print(i)





numbers: list[int] = list(range(1, 1000001))

for number in numbers:
    print(number)

# seconda possibilità senza fare la lista

# for number in range(1,100001):
#     print(number)