# Esercizio 8
# Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
# Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.
# Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

i = 1

while i <= 5:

    numero = int(input(f"Inserisci il numero {i} di cinque numeri tra 1 e 30: "))

    if numero >= 1 and numero < 31:
        
        print(f"Questo è il numero che hai inserito: {numero} e questo è il suo grafico: {'*' * numero}")
        i+= 1 
    
    else: 
        print("Il numero è fuori dal rango")
        
    

