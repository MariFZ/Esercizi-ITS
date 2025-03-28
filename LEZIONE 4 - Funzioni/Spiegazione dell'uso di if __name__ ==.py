# Spiegazione dell'uso di if __name__ == "__main__":

"""
Cosa significa?

    Questa riga serve a dire a Python:
    "Esegui questo codice solo se questo file viene avviato direttamente, 
    e NON se viene importato in un altro file.

Esempio pratico:

    Immagina di avere un file chiamato panini.py con questo codice:

def paninodoc(*elementi):
    print("\nGrazie del tuo ordine! Il tuo panino contiene:")
    for elemento in elementi:
        print(f"- {elemento}")
    print("Buon appetito!")

# Questo codice verrà eseguito solo se il file viene eseguito direttamente
if __name__ == "__main__":
    paninodoc("prosciutto", "formaggio", "pomodoro")

Caso 1: Eseguo direttamente panini.py

Se eseguo il file con:

python panini.py
Grazie del tuo ordine! Il tuo panino contiene:
- prosciutto
- formaggio
- pomodoro
Buon appetito!

Qui if __name__ == "__main__": è vero, quindi il codice dentro viene eseguito.

Caso 2: Importo panini.py in un altro file

Ora creo un altro file, chiamato ristorante.py, e voglio usare la funzione paninodoc da panini.py:

from panini import paninodoc

paninodoc("pollo", "lattuga", "maionese")

Se eseguo:

python ristorante.py

Output

Grazie del tuo ordine! Il tuo panino contiene:
- pollo
- lattuga
- maionese
Buon appetito

NOTA: Non viene stampato il panino con "prosciutto, formaggio, pomodoro" 
perché il codice sotto if __name__ == "__main__": 
non viene eseguito quando importo il file!

"""