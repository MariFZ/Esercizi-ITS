# ESERCIZIO 5 Match Statement and lists

# definisco la lista

ingredienti: list[str] = ["pomodoro", "mozzarella", "basilico"]

match ingredienti:

    # casi 1: se la lista contiene esattamente i tre ingredienti
    case ["pomodoro", "mozzarella", "basilico"]:
        print("Puoi fare una Caprese!")

    # case 2: se la lista inizia con pasta, pomodoro, l'asterisco permette di scrivere un'altro ingrediente
    case ["pasta", "pomodoro", *_]:
        print("Puoi fare la Pasta al Pomodoro!")

    # caso 3: se la lista contiene pane, prosciutto e formaggio
    case ["pane", "prosciutto", "formaggio"]:
        print("Puoi fare un Panino!")

    case _:
        print("Non saprei cosa consigliare…sperimenta!")

# esempio 

# Chiediamo all'utente di inserire gli elementi alla lista

# inizio con una lista vuota

lista_utente: list[str] = []

ingredienti: str =input("Inserisci gli ingredienti:")

lista_utente.append(ingredienti)



