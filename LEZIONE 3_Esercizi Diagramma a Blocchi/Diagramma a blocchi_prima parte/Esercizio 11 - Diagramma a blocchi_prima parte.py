# ESERCIZIO 11

# Sistema di prenotazione di posti

# Progetta un algoritmo per gestire la prenotazione dei posti in una sala che contiene 20 sedie libere. 
# L'utente può inserire una delle seguenti opzioni "prenota", "libera", "visualizza", "esci".
# Per ogni opzione:

''' se l'utente inserisce "prenota", se ci sono ancora sedie libere, decrementa di uno il numero di posti liberi;
    se l'utente inserisce "libera", incrementa di uno il numero di sedie libere;
    se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati;
    se l'utente inserisce "esci", termina l'algoritmo.

    Torna all'inserimento di una opzione finché l'utente non seleziona "esci".'''

sedie = 20

print("Sceglie una delle seguenti opzioni: 'prenota', 'libera', 'visualizza', 'esci'")
# scelta_utente = input("La tua scelta: ").strip().lower()

# opzione = input("Scrive la tua scelta dall'elenco appena letto: ")
                 
while True:
    
    opzione = input("Scrive la tua scelta dall'elenco appena letto: ")
    
    if opzione == "prenota":
        if sedie > 0:
            sedie += 1
            print(f"Posto prenotato.  Vuoi continuare con la prenotazione? Se no, sceglie 'esci'")
        else: 
            print("Non ci sono posti disponibili")
    
    elif opzione == "libera": 
        if sedie < 20:
            sedie -= 1
            print("La tua sedia è stata liberata. Vuoi continuare con la prenotazione? Se no, sceglie 'esci'")
        else:
            print("Tutte le sedie sono già libere")

    elif opzione == "visualizza":
        posti_occupati = 20 - sedie
        print(f"Le sedie disponibili sono queste: {sedie} e i posti occupati: {posti_occupati}. Vuoi continuare con la prenotazione? Se no, sceglie 'esci'")

    elif opzione == "esci":
        print("Arrivederci")
        break

