# Esercizio 3C-4. 
# 
# Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, 
# utilizzando un match statement, identifichi a quale categoria esso appartiene. L'animale deve essere classificato in una delle seguenti categorie:

# - Mammiferi: cane, gatto, cavallo, elefante, leone.
# - Rettili: serpente, lucertola, tartaruga, coccodrillo.
# - Uccelli: aquila, pappagallo, gufo, falco.
# - Pesci: squalo, trota, salmone, carpa.

# Se l'animale non appartiene a nessuna delle categorie sopra elencate,  
# mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.

# Suggerimento: Utilizzare una lista per ognuna della quattro categorie.



mammiferi: list[str] = ["cane", "gatto", "cavallo", "elefante", "leone"]
rettili: list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli: list[str] = ["aquila", "pappagallo", "gufo", "falco"]
pesci: list[str] = ["squalo", "trota", "salmone", "carpa"]

animale: str = (input("Inserisci il nome di un animale che per identificare a quale categoria appartiene: "))

match animale:

    case animale if animale in mammiferi:
        print(f"L'animale che hai scritto: \"{animale}\" appartiene alla categoria dei Mammiferi!")

    case animale if animale in rettili:
        print(f"L'animale che hai scritto: \"{animale}\" appartiene alla categoria dei rettili!")

    case animale if animale in uccelli:
        print(f"L'animale che hai scritto: \"{animale}\" appartiene alla categoria degli Uccelli!")

    case animale if animale in pesci:
        print(f"L'animale che hai scritto: \"{animale}\" appartiene alla categoria degli pesci!")

    case _:
        print(f"Non so dire in quale categoria classificare l'animale \"{animale}\"! ")

