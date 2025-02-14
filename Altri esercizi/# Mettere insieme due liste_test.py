
sedie = 50

# Loop per gestire le opzioni

while True: 
    print("Inserisce una delle seguenti opzioni: 'prenota', 'libera', 'visualizza', 'esci'")
    scelta_utente = input("La tua scelta: ")  
    
    if scelta_utente == "prenota":
        if sedie > 0:
            sedie -= 1
            print(f"Posto prenotato. Totale di sedie libere: {sedie}")
    
    elif scelta_utente == "libera":
        if sedie < 50:
            sedie += 1
            print(f"Totale di sedie libere è =  {sedie}")

    elif scelta_utente == "visualizza":
        posti_occupati = 50 - sedie 
        print(f"Totale di sedie libere è =  {sedie}  e posti occupati sono  {posti_occupati}")
    
    elif scelta_utente == "esci":
          print("Grazie e arrivederci.")
          break
