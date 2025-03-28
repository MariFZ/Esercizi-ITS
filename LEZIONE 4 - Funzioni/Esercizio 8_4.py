# ESERCIZIO 8.4
# Camicie grandi: 

# Modificare la funzione make_shirt() in modo che le camicie siano grandi per impostazione predefinita con un messaggio che recita I love Python. 
# Create una camicia grande e una media con il messaggio predefinito e una camicia di qualsiasi taglia con un messaggio diverso.
# Richiamate la funzione una sola volta utilizzando gli argomenti posizionali per creare una maglietta. 
# Richiamare la funzione una seconda volta utilizzando gli argomenti delle parole chiave.

def make_shirt(taglia: str = "XL", messaggio: str = "I love Python") -> str:

     print(f"La camicia taglia {taglia} dice: {messaggio} ")

# creazione maglia taglia grande e media con messaggio predefinito con argomenti posizionali 

# richiamo la funzione per i valori predefiniti 
make_shirt()

# richiamo la funzione cambiando la misura ma lasciando il messaggio predefinito
make_shirt("M")

# chiamata per parola chiave
make_shirt(taglia= "S", messaggio= "Ciao Roma!" )

