# Esercizio 6

# Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.
# Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.

primo_numero = int(input("Inserisci il primo numero: "))

secondo_numero = int(input("Inserisci il secondo numero: "))

prodotto = 1


# se il primo numero è maggiore
''' Il range si fa del numero più piccolo a quello più grande, 
    e si aumenta di 1 perchè range non prende l'ultimo numero'''
if primo_numero > secondo_numero:
    for numero in range(secondo_numero, primo_numero+1):
        prodotto *= numero

# se il secondo numero è maggiore
    '''il range parte sempre dal numero più piccolo, 
        fino al numero più grande + 1'''
    
elif primo_numero > secondo_numero:
    for numero in range(primo_numero, secondo_numero+1):
        prodotto *= numero

# in caso che i numeri inseriti siano uguali
else:
    prodotto = primo_numero








# questa soluzione ha due errori:

'''
1.  Non aumenta il valore del rango, qui l'ultimo numero non viene aggiornato'
2. Il prodotto si fa solo con il valore del primo for, non entre i numeri'''

if primo_numero < secondo_numero:
    for i in range (primo_numero,secondo_numero):
        prodotto = (primo_numero*i*secondo_numero) # in questa pa

    print(f"Il prodotto tra il primo numero: {primo_numero} e il secondo numero: {secondo_numero} è: {prodotto}")

elif primo_numero > secondo_numero:
    for i in range (secondo_numero, primo_numero+1):
        prodotto = (secondo_numero*i*primo_numero)

    print(f"Il prodotto tra il primo numero: {primo_numero} e il secondo numero: {secondo_numero} è: {prodotto}")
    