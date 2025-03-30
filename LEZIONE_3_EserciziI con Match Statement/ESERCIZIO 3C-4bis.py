# CREO IL DIZIONARIO VUOTO
login_utente: dict[str, any] = {}

# INSERISCO LA CHIAVE/VALORE NOME
nome_utente: str = input("Inserisci il tuo nome: ")
login_utente["nome"] = nome_utente

# INSERISCO LA CHIAVE/VALORE RUOLO UTENTE
ruolo_utente: str = input("Inserisci il tuo ruolo: (Admin/Moderatore/Utente Adulto/Utente Minorenne/Ospite) ").capitalize()
login_utente["ruolo"] = ruolo_utente

# INSERISCO LA CHIAVE/VALORE ETA E LA CONVERTO IN INTERO
try:
    eta_utente: int = int(input("Inserisci la tua età: "))  
    login_utente["eta"] = eta_utente
except ValueError:
    print("Errore! Devi inserire un numero intero per l'età.")
    exit()

# MATCH CASE

match login_utente:
    case {"nome": name, "ruolo": "Admin"}:
        print(f'Benvenuto "{name}". Accesso completo a tutte le funzionalità.')

    case {"nome": name, "ruolo": "Moderatore"}:
        print(f'Benvenuto "{name}". Può gestire i contenuti ma non modificare le impostazioni.')

    case {"nome": name, "ruolo": "Utente Adulto", "eta": edad} if edad >= 18:
        print(f'Benvenuto "{name}". Accesso standard a tutti i servizi.')

    case {"nome": name, "ruolo": "Utente Minorenne", "eta": edad} if edad < 18:
        print(f'Benvenuto "{name}". Accesso limitato! Alcune funzionalità sono bloccate.')

    case {"nome": name, "ruolo": "Ospite"}:
        print(f'Benvenuto "{name}". Accesso ristretto! Solo visualizzazione dei contenuti.')

    case _:
        print("Attenzione! Ruolo non riconosciuto! Accesso Negato!")

