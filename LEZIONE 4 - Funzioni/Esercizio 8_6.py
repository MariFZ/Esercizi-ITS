# 8.6
# Nomi di città

# Scrivete una funzione chiamata città_paese() che accetta il nome di una città e il suo paese. 
# La funzione deve restituire una stringa formattata come questa: "Santiago, Cile". 
# Richiamate la funzione con almeno tre coppie città-paese e stampate i valori restituiti.

def città_paese(citta: str, paese: str):

    print(f"\"{citta}, {paese}\" ")

città_paese("Barcellona", "Spagna")

città_paese("Londra", "Parigi")

città_paese("Milano", "Italia")