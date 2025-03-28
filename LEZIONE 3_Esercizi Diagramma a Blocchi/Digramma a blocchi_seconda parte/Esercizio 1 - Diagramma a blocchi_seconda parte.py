# ESERCIZIO 1 Algoritmi e Diagrammi a blocchi #2

# Sistema di gestione per un parcheggio
'''Progetta un algoritmo per la gestione dell'ingresso e dell'uscita di veicoli da un parcheggio 
con un numero massimo di posti dato in input. 
L'utente può inserire una delle seguenti opzioni "ingresso", "uscita", "stato", "esci". 

Per ogni opzione:

    se l'utente inserisce "ingresso", verifica se ci sono posti disponibili, quindi incrementa il numero di posti occupati;
    se l'utente inserisce "uscita", verifica che ci siano veicoli nel parcheggio, quindi decrementa il numero di posti occupati;
    se l'utente inserisce "stato", mostra il numero dei posti liberi e il numero dei posti occupati;
    se l'utente inserisce "esci", termina l'algoritmo.'''

posti_max = int(input("Inserisci il numero massimo di posti del parcheggio: "))

print("Sceglie una delle seguenti opzioni: 'ingresso', 'uscita', 'stato', 'esci'")

posti_disponibili = posti_max
posti_occupati = 0


while True: 

    opzione = input("Inserisce la tua opzione: ")

    if opzione == "ingresso":
        if posti_disponibili > 0:
            posti_occupati += 1 
            posti_disponibili -=1
            print("Veicolo parcheggiato con succeso")
            
        else: 
            print("Il parcheggio è pieno")
    
    elif opzione == "uscita":
        if posti_occupati > 0:
            posti_occupati += 1
            posti_disponibili -= 1
            print("Veicolo uscito con succeso")

        else:
            print("Il parcheggio è già vuoto")

    elif opzione == "stato":
        print(f"I posti occupati sono: {posti_occupati} e i posti liberi {posti_disponibili}")

    elif opzione == "esci":
        print("Arriverderci")
        break

