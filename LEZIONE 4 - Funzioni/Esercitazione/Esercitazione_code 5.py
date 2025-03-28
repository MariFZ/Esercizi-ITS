# ESERCIZIO 5

# Scrivi una funzione che prende una lista di parole 
# e restituisce una lista contenente la lunghezza di ciascuna parola.

def lenparole(lista: list[str]) -> list[str]:

    parole: list[int] = []

    for parola in lista:
        
        parole.append(f"{parola}: {len(parola)}")
       
    return parole

lista_parole: list[str] = ["scatola", "penna", "quadro", "lampada", "computer", "mouse"]

print(f"Questa è la lunguezza delle parole che sono nella lista: {lenparole(lista_parole)}")

