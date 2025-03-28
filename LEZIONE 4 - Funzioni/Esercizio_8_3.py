# ESERCIZIO 8.3
# Maglietta
 
# Scrivete una funzione chiamata make_shirt() che accetti una taglia e il testo di un messaggio da stampare sulla maglietta. 
# La funzione deve stampare una frase che riassuma la taglia della maglietta e il messaggio stampato su di essa. 
# Richiamate la funzione una sola volta utilizzando gli argomenti posizionali per creare una maglietta. 
# Richiamate la funzione una seconda volta utilizzando gli argomenti delle parole chiave.

from typing import Any
'''per importare il tipo Any dopo la definzione delle varibili'''


def make_shirt(taglia, testo) -> Any:
    
    print(f"La taglia che hai scelto: {taglia}: {testo}")
    

# Chiamata della funzione per posizione
make_shirt("S", "Domani dormo")

# # Chiamata della funzione per parola chiave
make_shirt(taglia="M", testo= "How are you?" )





