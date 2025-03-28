# ESERCIZIO 2

# Scrivi una funzione che prende una stringa e restituisce la stringa invertita

# def paroleinvertite(stringa) -> str:  # creo la funzione

#     return stringa[::-1]        # con il metodo slices imposto lo scorrimento dentro della stringa, con il -1 dico che deve iniziare dalla fine

# # Creo la variabile stringa che invertirò

# parola: str = ("amor")

# # Uso il print per chiamarè la funzione, senza creare una variabile in più

# print(f"Questa è la parola originale: \"{parola}\" e questa invece è la parola invertita usando la funzione: \"{paroleinvertite(parola)}\"")


# ----------------------------------------------
# Conversione della parola usando il ciclo while

# Creo la funzione
def paroleinvertite(stringa) -> str:
    return stringa

# Creo il ciclo while

    # 1) Creo le variabili

parola: str = ("amor")      # parola originale
invert: str = ("")          # stringa vuota che conterrà le parole invertite
i = len(parola) -1          # prendo la lunghezza 

while i >= 0:
    invert += parola[i]
    i-= 1
        
paroleinvertite(invert)

print(f"Questa è la parola originale: \"{parola}\", e questa è la parola invertita: \"{invert}\" usando il ciclo while")
