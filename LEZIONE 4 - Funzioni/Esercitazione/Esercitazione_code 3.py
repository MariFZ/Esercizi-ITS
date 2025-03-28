# ESERCIZIO 3

# Scrivi una funzione che prende una lista di parole 
# e restituisce una lista contenente solo le parole che iniziano con una lettera specificata.

# Creo la variabile, che contiene una variabile "lista" e un'altra variabile: "lettera"

def lettera_specifica(lista: list[str], lettera: str) -> list[str]:

    lista_parole: list[str] = []        # creo una lista vuota che conterrà le parole che iniziano con la stessa lettera

    for parola in lista:                # inizio il ciclo for che andrà a vedere ogni parola nella lista
        if parola[0] == lettera:        # analizzo che la parola all'indice 0 [0] inizia con la lettera
            lista_parole.append(parola) # se si, aggiungo la parola alla lista
    
    return lista_parole                 # ritorno il valore per poter usarlo dopo

# Creo la lista di parole da verificare

linea: list[str] = ["amore", "cane", "animale", "cellulare", "alfa"]
lettera = "c"

print(f"Questa è la lista originale: {linea} e questa è la lista nuova con le parole che iniziano con la lettera \"{lettera}\": \"{lettera_specifica(linea, lettera)}\"")