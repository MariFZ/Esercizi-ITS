# ESERCIZIO 8.12

# Panini
# Scrivete una funzione che accetti un elenco di elementi che una persona desidera in un panino. 
# La funzione deve avere un parametro che raccolga tanti elementi quanti ne fornisce la chiamata alla funzione 
# e deve stampare un riepilogo del panino ordinato. Chiamate la funzione tre volte, utilizzando ogni volta un numero diverso di argomenti.

# Sandwiches
# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

def paninodoc(*elementi): # con * posso scrivere quanti elementi voglio!

    # Faccio un print per indicare che l'ordine sta iniziando.  Con \n do un spazio, per il secondo print
    print("\nGrazie del tuo ordine! Adesso iniziamo a fare il tuo panino")

    # Chiamo ogni elemento, e lo stampo uno ad uno
    for elemento in elementi:
        print(f"Ho aggiunto \"{elemento}\" al tuo panino")
    print("Il tuo panino è pronto!")


# richiamo la funzione con i valori dentro
paninodoc("carne", "formaggio", "pancetta")
paninodoc("pollo", "pancetta", "pane", "cocacola")


































# def make_sandwich(*items):
#     """Make a sandwich with the given items."""
#     print("\nI'll make you a great sandwich:")
#     for item in items:
#         print("  ...adding " + item + " to your sandwich.")
#     print("Your sandwich is ready!")

# make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
# make_sandwich('turkey', 'apple slices', 'honey mustard')
# make_sandwich('peanut butter', 'strawberry jam')