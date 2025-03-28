# ESERCIZIO 8.15

# Printing Models
# Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
# Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

# Note: The text refers to print_models.py, but it should say printing_models.py.

# printing_functions.py:

# Mettete le funzioni dell'esempio printing_models.py in un file separato chiamato printing_functions.py. 
# Scrivete una dichiarazione di importazione all'inizio di printing_models.py e modificate il file per utilizzare le funzioni importate.


"""Importare una funzione specifica"""

from Esercizio_8_12 import paninodoc


paninodoc("pollo", "formaggio", "insalata")

from Esercizio_8_14 import makecar as mc

macchina2 = mc('Punto', 'Vecchio modello', color='verde', autoradio=False)

print(macchina2)








