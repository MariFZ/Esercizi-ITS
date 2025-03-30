# Gioco 
# Indovina un numero

# si crea una funzione che prenderà la logica del gioco

import random
'''
Prima dobbiamo importare la sentenza. La sentenza è un modulo 
che contiene file che contiene funzioni o elementi utili.

Il metodo random: permette lavorare con processi aleatori
Come funziona
* Importarlo: import random
* Scrive il modulo che abbiamo importato:random
* Chiamo la funzione: la funzione si chiama: randint(): random intero.
* Come funziona? 
------  randint(a,b): Prende due parametri: a e b
ritorna un intero aleatorio N uguale a questo: a <= N <= b 
* Dove N è >= a (il primo parametro scritto) e 
* Dove N è <= b (il secondo paramentro).
-----In altre parole è il limite superiore o inferiore

--- esiste anche un'altra che si chiama: randrange: Ritorna un elemento de
range(start, stop, step) selezionato aleatoriamente. E' uguale a dire: 
choice(range(start, stop, step))------

'''
def indovina_il_numero(x):
    '''x rappresenta il limite superior del intervallo valido di valori:
    per esempio: Indovina un numero da 1 a 15, 15 sarebbe il valore di x'''

    print("==========================================================")
    print("               Benvenut@ al gioco!!!!                     ")
    print("Il gioco consiste in indovinare il numero creato per il PC")

# dobbiamo salvare in una variabile il numero aleatorio che il PC


    numero_aleatorio:int = random.randint(1,x) # numero tra 1 e X, compressi
    '''1 sarebbe il numero inferiore '''

    # assegno alla variabile un valore, che in questo caso sarebbe 0
    # affinchè non venga generato dal PC
    indovina = 0


    # inizio un ciclo while perchè devo ripetere un'azione un numero inderterminato di volte

    while indovina != numero_aleatorio:
        # l'usuario ingressa un numero
        indovina = int(input(f"Indovina un numero tra 1 e {x}: ")) # sarà un intero e sovrascrivo il valore della variabile: "indovina"

        if indovina < numero_aleatorio:
            print("Provaci ancora, questo numero è molto piccolo!")
        
        elif indovina > numero_aleatorio:
            print("Provaci ancora, questo numero è molto grande")


    print(f"Auguri! Hai indovinato il numero {numero_aleatorio} correttamente")


indovina_il_numero(10)
'''scrivendo 10 specifico che il numero sarà tra 1 e 10 '''