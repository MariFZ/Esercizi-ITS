# ESERCIZIO 3C-7. 
# Si scriva un programma che computi la statistica di otto lanci di una moneta.
# Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
# Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

# NOTA.
# Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
# Usare il match statement.

# Expected Output:

# Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".

# Lancio 1: t
# Lancio 2: c
# Lancio 3: t
# Lancio 4: t
# Lancio 5: c
# Lancio 6: c
# Lancio 7: t
# Lancio 8: t

# Totale "testa": 5
# Percentaule "testa": 62.50%

# Totale "croce": 3
# Percentuale "croce": 37.50%


somma_testa: int = 0
somma_croce: int = 0
i: 1

for i in range(1,9):
    i < 9

    lanci: str = input("Inserisci: 't' o 'T se e' uscito 'testa', mentre inserisci 'c' o 'C' se è uscito 'croce' (t/c)): ")

    match lanci:

        # IN CASO DI T
        case "t"|"T": 
            somma_testa += 1
            i += 1
    
        # IN CASO DI C

        case "c"|"C":
            somma_croce += 1
            i += 1
    
        case _:
            print("Non hai inserito un valore corretto")

print(f"Totale testa è: {somma_testa} \nPercentuale testa: {(somma_testa/i)*100:.2f}%, \nTotale croce: {somma_croce}\nPercentuale croce: {(somma_croce/i)*100:.2f}%.")

