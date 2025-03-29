# Esercizio 3C-5. 
# Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario. 
# Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. 
# Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:


# CREO IL DIZIONARIO VUOTO
login_utente: dict[str,int] = {}

# INSERISCO LA CHIAVE/VALORE NOME
nome_utente: str = input("Inserisci il tuo nome: ")
login_utente["nome"] = nome_utente

# INSERISCO LA CHIAVE/VALORE RUOLO UTENTE

ruolo_utente: str = input("Inserisci il tuo ruolo: (admin/moderatore/utente/ospite)")
login_utente ["ruolo"] = ruolo_utente

# INSERISCO LA CHIAVE/VALORE ETA
eta_utente: int = int(input("Inserisci la tua età: "))
login_utente["eta"] = eta_utente




match login_utente:
   
    case {"nome": name, "ruolo": "admin"}:      # name qui è una variabile volatile che mi prende il valore della chiave di nome
        print(f"Benvenuto \"{name}\". Accesso completo a tutte le funzionalità") 
    
    case {"nome": name, "ruolo": "moderatore"}:
        print(f"Benvenuto \"{name}\". Può gestire i contenuti ma non modificare le impostazioni") 
    
    case {"nome": name, "ruolo": "utente", "eta": age} if age >= 18:   # age qui è una variabile volatile che mi prende il valore della chiave età
        print(f"Benvenuto \"{name}\". Accesso standard a tutti i servizi.") 

    case {"nome": name, "ruolo": "utente", "eta": age} if age < 18:
        print(f"Benvenuto \"{name}\"Accesso limitato! Alcune funzionalità sono bloccate.")

    case {"nome": name, "ruolo": "ospite"}:
        print(f"Benvenuto \"{name}\". Accesso ristretto! Solo visualizzazione dei contenuti..")

    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")

