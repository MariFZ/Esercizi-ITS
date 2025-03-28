# ESERCIZIO 9

# Scrivi una funzione che prende una lista di parole 
# e restituisce una lista contenente solo le parole palindrome.

def lista_parole(lista: list[str]) -> list[str]:

    palindrome: list[str] = []

    for parola in lista:
        if parola[::-1] == parola:
            palindrome.append(f"{parola} = {parola[::-1]}")
    
    return palindrome

parole_palindrome: list[str] = ["esse", "casa", "osso", "metro" "aerea", "aveva", "ingegni", "ovattavo", "computer"]

print(f"Queste sono le parole palindrome: {lista_parole(parole_palindrome)}")