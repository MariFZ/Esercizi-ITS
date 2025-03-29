# # ESERCIZIO 6 - Match Statement and dictionaries

# # definire il dizionario

# user = {"nome": "Luca", "ruolo": "admin"}
# # match statement

# match user:

#     case {"nome": name, "ruolo": "admin"}:      # name qui è una variabile volatile che mi prende il valore della chiave di nome
#         print(f"Benvenuto amministratore {name}") 

#     #case {"nome": user["nome"],"ruolo": "admin"}: # ATTENZIONE: non si può cercare per il valore della chiave user["nome"] da errore di sintassi
#         # print(f"Benvenuto amministratore {user["nome"]}") : NEL PRINT E' VALIDO

#     case {"nome": name, "ruolo": "utente"}:
#         print(f"Benvenuto utente {name}")
    
#     case _:
#         print("Ruolo non riconosciuto")


# ESEMPIO CON INPUT DINAMICO

# Chiediamo all'utente di inserire il nome e il ruolo

# nome = input("Inserisci il tuo nome: ")
#ruolo = input("Inserisci il tuo ruolo (admin/utente): ")

# Creiamo il dizionario 'user' in base all'input

# user = {"nome": nome, "ruolo": ruolo}

admin: dict[str] = {"admin1": "Jean Paul", "admin2": "Mari", "admin3": "Andrew"}
utenti: dict[str] = {"utente1" : "Juan", "utente2": "Pauli"}


# Creiamo il dizionario 'user' in base all'input
# user = {"nome": nome, "ruolo": ruolo}

nome = input("Inserisci il tuo nome: ")

# Dizionari degli admin e degli utenti
admin: dict[str] = {"admin1": "Jean Paul", "admin2": "Mari", "admin3": "Andrew"}
utenti: dict[str] = {"utente1": "Juan", "utente2": "Pauli"}

# Inizio del match statement
match nome:
    
    # Controlliamo se il nome è tra i valori degli amministratori
    case nome if nome in admin.values():
        print(f"Benvenuto amministratore {nome}")
    
    # Controlliamo se il nome è tra i valori degli utenti
    case nome if nome in utenti.values():
        print(f"Benvenuto utente {nome}")
    
    # Caso di default: ruolo non riconosciuto
    case _:
        print("Ruolo non riconosciuto")

