# ESERCIZIO 7

# Scrivi una funzione che prende una lista di parole 
# e restituisce la parola più lunga.

def parola_lunga(lista: list[str]) -> tuple[str, int]:

    piu_lunga: str = (lista[0])

    for parola in lista: 
        if len(parola) > len(piu_lunga):
            piu_lunga = parola
    
    return piu_lunga, len(piu_lunga)

lista_parole: list[str] = ["computer", "lampada", "musica", "tastiera", "scatola", "mouse"]

print(f"Questa è la parola più lunga della lista: {parola_lunga(lista_parole)}")

