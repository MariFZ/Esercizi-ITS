sedie = 50

# Loop principale per gestire le opzioni
while True:
    # Richiesta opzione all'utente
    print("Inserisci una delle seguenti opzioni: 'prenota', 'libera', 'visualizza', 'esci'")
    scelta_utente = input("La tua scelta: ").strip().lower()

    if scelta_utente == "prenota":
        if sedie > 0:
            sedie -= 1
            print(f"Posto prenotato. Totale di sedie libere: {sedie}.  Vuoi continuare con la prenotazione? Se no, sceglie 'esci'")
    
        else:
            print("Nessuna sedia disponibile per la prenotazione.")

    elif scelta_utente == "libera":
        if sedie < 50:
            sedie += 1
            print(f"Posto liberato. Totale di sedie libere: {sedie}. Vuoi continuare con la prenotazione? Se no, sceglie 'esci'")
        else:
            print("Tutte le sedie sono già libere.")

    elif scelta_utente == "visualizza":
        posti_occupati = 50 - sedie
        print(f"Totale di sedie libere: {sedie}, posti occupati: {posti_occupati}.  Vuoi continuare con la prenotazione? Se no, sceglie 'esci'")

    elif scelta_utente == "esci":
        print("Grazie e arrivederci.")
        break

    else:
        print("Opzione non valida. Riprova.")

