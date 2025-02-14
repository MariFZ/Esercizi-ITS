# ESERCIZIO 8 
# Determinare la somma dei numero dentro un intervallo
# Progettare un algoritmo che chieda all’utente di inserire due valori interi positivi 𝐴 e 𝐵 con 𝐴 < 𝐵. Se i valori non rispettano le condizioni, mostrare un messaggio di errore e terminare. Se i valori sono validi, calcolare la somma di tutti i numeri interi compresi tra 𝐴 e 𝐵 (inclusi) e mostrare il risultato.

A = int(input("Inserire A: ")) # Read A
B = int(input("Inserire B: ")) # Read B

if A % 1 == 0 and B % 1 == 0 and A >= 0 and B >= 0 and A < B : 
    somma = 0 
    '''while A <= B:    # CICLO WHILE lE variabili A e B devono essere float
        somma += A
        A += 1 '''
    
    '''for n in range(A, B+1):  #  CICLO FOR lE variabili A e B devono essere int
        somma += n'''
    
    somma = sum(range(A, B+1))  # Questa è come si può scrivere in Python che significa dal numero A al B, salta un numero e somma

    print(f"Il risultato è {somma}")

else:
    print(f"Errore: i valori A= {A}) e B= {B} non sono validi")

# ESERCIZIO 9

n = int(input("Inserisce un divisore positivo: "))
num_div = 0
inseriti = 0

if n > 0:
    continua = True

    while continua and inseriti < 10:
        num = int(input("Inserisce un valore:  "))

        if num % n == 0:
            num_div += 1

        inseriti += 1

        scelta = input("Vuoi continuare? ( default: si) ")
        if scelta.lower() == "no": 
            continua = False

# fine del while

print(f"Hai inserito  {num_div} numeri divisibili per {n}")

else:
    print("Errore: Il divisore deve essere positivo")
