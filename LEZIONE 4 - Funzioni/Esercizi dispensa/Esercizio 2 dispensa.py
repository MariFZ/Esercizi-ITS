# ESERCIZIO 2 DISPENSA

# Scrivete una funzione check_length(), che prende una stringa come argomento. 
# Utilizzando if/ else, verificate se la lunghezza della stringa è maggiore, minore o uguale a 10 caratteri.

def check_length(a:str) -> int:

    if len(a) > 10:
        print(f"La stringa {a} è maggiore di 10 caratteri")
    elif len(a) < 10:
        print(f"La stringa {a} è minore di 10 caratteri")
    else: 
        print(f"La stringa {a} è uguale a 10 caratteri")

check_length("domani")