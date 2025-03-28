# ESERCIZIO 3. Sistema di registrazione degli studenti a corsi

# Progetta un algoritmo che gestisca l'iscrizione degli studenti a corsi disponibili in una università. 
# Per ogni corso ci sono un massimo di 100 posti liberi. Richiesto il nome del corso, 
# mostra un menu con le seguenti opzioni "iscrivi", "annulla", "visualizza", "elimina", ed "Esci".

# se l'utente inserisce "iscrivi", verifica se ci sono posti disponibili per il corso, quindi incrementa il numero di posti occupati;
# se l'utente inserisce "annulla", decrementa il numero di posti occupati;
# se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati nel corso;
# se l'utente inserisce "elimina", elimina il corso e richiedi un nuovo corso;
# se l'utente inserisce "esci", termina l'algoritmo.

tot_posti_biologia = 100

tot_posti_matematica = 100

tot_posti_arte = 100

posti_occupati_biologia = 0
posti_occupati_matematica = 0
posti_occupati_arte = 0

while True:
    opzione_1 = str(input("Scegli il corso al quale vuoi iscriverti: \n'Biologia', 'Matematica', 'Arte': "))

    if opzione_1 == 'Biologia':
        opzione = str(input("Inserisci la scelta che vorresti fare: 'iscrivermi', 'annullare', 'visualizzare', 'eliminare', 'esci'"))
        
        if opzione == 'iscrivermi':
            if tot_posti_biologia >= posti_occupati_biologia:
                posti_occupati_biologia +=1
                print("Sei stato iscritto correttamente, vuoi continuare?")
            
            else: 
                print("Nessun posto disponibile")
                

        elif opzione == 'annullare':
            if posti_occupati_biologia > 0:
                posti_occupati_biologia-=1
        
        elif opzione == 'visualizzare':
            print(f"I posti ancora disponibili per questo il corso di Biologia sono: {tot_posti_biologia - posti_occupati_matematica} e i posti occupati per questo corso sono: {posti_occupati_biologia}")
        
        elif opzione == 'elimina':
            print("Il corso Biologia è stato eliminato. Scegli il corso al quale vuoi iscriverti: 'Matematica', 'Arte'")
            tot_posti_biologia = 0
            posti_occupati_biologia = 0
        
        elif opzione == 'esci':
            print("Arrivederci")
            break

    if opzione_1 == 'Matematica':
        opzione = str(input("Inserisci la scelta che vorresti fare: 'iscrivermi', 'annullare', 'visualizzare', 'eliminare', 'esci'"))
        if opzione == 'iscrivermi':
            if tot_posti_matematica >= posti_occupati_matematica:
                posti_occupati_matematica +=1
                print("Sei stato iscritto correttamente, vuoi continuare?")
            
            else: 
                print("Nessun posto disponibile")


        elif opzione == 'annullare':
            posti_occupati_matematica -=1
        
        elif opzione == 'visualizzare':
            print(f"I posti ancora disponibili per questo il corso di Matematica sono: {tot_posti_matematica - posti_occupati_matematica} e i posti occupati per questo corso sono: {posti_occupati_matematica}")
        
        elif opzione == 'elimina':
            print("Il corso Matematica è stato eliminato. Sceglie il corso al quale vuoi iscriverti: 'Biologia', 'Arte'")
            tot_posti_matematica = 0
            posti_occupati_matematica = 0
            
        
        elif opzione == 'esci':
            print("Arriverci")
            break

    if opzione_1 == 'Arte':
        opzione = str(input("Inserisci la scelta che vorresti fare: 'iscrivermi', 'annullare', 'visualizzare', 'eliminare', 'esci'"))
        if opzione == 'iscrivermi':
            if tot_posti_arte >= posti_occupati_arte:
                posti_occupati_arte +=1
                print("Sei stato iscritto correttamente, vuoi continuare?")
            
            else: 
                print("Nessun posto disponibile")

        elif opzione == 'annullare':
            posti_occupati_arte -=1
        
        elif opzione == 'visualizzare':

            print(f"I posti ancora disponibili per il corso di Arte sono: {tot_posti_arte - posti_occupati_arte} e i posti occupati per questo corso sono: {posti_occupati_arte}")
        
        elif opzione == 'elimina':
            print("Il corso Arte è stato eliminato. Sceglie il corso al quale vuoi iscriverti: 'Biologia', 'Arte'")
            tot_posti_arte = 0
            posti_occupati_arte = 0
        
        elif opzione == 'esci':
            print("Arriverci")
            break

# print(f"Queste sono i risultati delle iscrizioni per i corsi, \n Matematica: 'Questi sono i posti occupati: {posti_occupati_matematica} e questi sono i posti disponibili: {posti_disponibili_matematica}. \n Biologia: 'Questi sono i posti occupati: {posti_occupati_biologia} e questi sono i posti disponibili: {posti_disponibili_biologia} \n Arte: 'Questi sono i posti occupati: {posti_occupati_arte} e questi sono i posti disponibili: {posti_disponibili_arte} ")
