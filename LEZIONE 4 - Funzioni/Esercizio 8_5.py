# ESERCIZIO 8.5

# Città: 
# Scrivete una funzione chiamata describe_city() che accetti il nome di una città e il suo paese. 
# La funzione deve stampare una frase semplice, ad esempio Reykjavik è in Islanda. 
# Date al parametro del paese definito. Richiamate la funzione per tre città diverse, di cui almeno una non appartenente al paese predefinito.

def describe_city(citta: str, paese: str = "Italia"): 
    
    print(f"{citta} è in {paese}.")


describe_city(citta= "Roma")
describe_city(citta= "Barcellona", paese= "Spagna")