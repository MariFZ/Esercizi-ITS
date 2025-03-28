# Esercizio 4

# Scrivete una funzione check_each(), che prenda come argomento un elenco di numeri. 
# Utilizzando un ciclo for, iterate attraverso l'elenco.
# Per ogni numero, stampare "più grande" se è più grande di 5, 
# "più piccolo" se è più piccolo di 5 e "uguale" se è uguale a 5.

def check_each(numeri: list[int]):

    for i in numeri:
        if i > 5:
            print(f" Il numero: {i} è \"più grande\" di 5")
        elif i < 5:
            print(f" Il numero: {i} è \"più piccolo\" di 5")
        else:
            print(f" Il numero: {i} è \"uguale\" a 5")


lista: list[int] = [2,5,3,7,8,10]

check_each(lista)