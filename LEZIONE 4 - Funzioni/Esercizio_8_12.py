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
    """Funzione che stampa la composizione di un panino con gli ingredienti scelti"""


    # Faccio un print per indicare che l'ordine sta iniziando. 
    # Con \n do un spazio, per il secondo print"""
    
    print("\nGrazie del tuo ordine! Adesso iniziamo a fare il tuo panino")

    # Chiamo ogni elemento, e lo stampo uno ad uno"""

    for elemento in elementi:
        print(f"Ho aggiunto \"{elemento}\" al tuo panino")
    print("Il tuo panino è pronto!")


# Per importare una funzione devo scrivere: 
   
    # "if __name__== "__main__": 
    #   e dopo la funzione con gli argomenti
    #  paninodoc("carne", "formaggio", "pancetta")
   

if __name__== "__main__":

# richiamo la funzione con i valori dentro
    paninodoc("carne", "formaggio", "pancetta")
    paninodoc("formagggio", "doppia carne", "pancetta")


  

 