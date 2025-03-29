# ESERCIZIO 3C-9

# Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto (x, y) e salvi le coordinate inserite in una tupla. 
# Utilizzare il  match statement per determinare la sua posizione del punto inserito nel piano cartesiano:

# - Origine → Se il punto è (0,0), stampare: "Il punto si trova nell'origine."
# - Asse X → Se y = 0, stampare: "Il punto si trova sull'asse X."
# - Asse Y → Se x = 0, stampare: "Il punto si trova sull'asse Y."
# - Primo quadrante → Se x > 0 e y > 0, stampare: "Il punto si trova nel primo quadrante."
# - Secondo quadrante → Se x < 0 e y > 0, stampare: "Il punto si trova nel secondo quadrante."
# - Terzo quadrante → Se x < 0 e y < 0, stampare: "Il punto si trova nel terzo quadrante."
# - Quarto quadrante → Se x > 0 e y < 0, stampare: "Il punto si trova nel quarto quadrante."

# Expected Output:

# Inserisci la coordinata X: 0
# Inserisci la coordinata Y: 0
# Output: Il punto (0,0) si trova nell'origine.

# - - - - - - - - - - - - - - - - - - - - - -

# Inserisci la coordinata X: 3
# Inserisci la coordinata Y: 5
# Output: Il punto (3,5) si trova nel primo quadrante.

# - - - - - - - - - - - - - - - - - - - - - - - - -

# Inserisci la coordinata X: 4
# Inserisci la coordinata Y: 0
# Output: Il punto (4,0) si trova sull'asse X.

# Chiedi all'utente di inserire le coordinate
x: int= int(input("Inserisce la coordinata x: "))
y: int= int(input("Inserisce la coordinata y: "))

# Definisce la tupla con le coordinate
coordinate: tuple[int] = ()


lista: list[int] = list(coordinate)  # Convertiamo la tupla in una lista

lista.append(x)     # Aggiungiamo un valore X
lista.append(y)     # Aggiungiamo un valore y

print(lista)
coordinate: tuple[int] = tuple(lista)  # Riconvertiamo in tupla


match coordinate:

    # Se il punto è (0,0)
    case (0, 0):
        print("Il punto si trova nell'origine")

    # Se y = 0
    case (x, 0):
        print("Il punto si trova sull'asse X")

    # Se x = 0
    case (0, y):
        print("Il punto si trova sull'asse Y")

    # Se x > 0 e y > 0, per esempio: 3,5
    case (x, y) if x > 0 and y > 0:
    
        print("Il punto si trova nel primo quadrante")

    # Se x < 0 e y > 0, per esempio -3, 2
    case (x, y) if x < 0 and y > 0:
        print("Il punto si trova nel secondo quadrante!")

    # Se x < -3 e y < -4
    case (x, y) if x < 0 and y < 0:
        print("Il punto si trova nel terzo quadrante.")
    
    
    case _:
        print("Il punto si trova nel quarto quadrante")