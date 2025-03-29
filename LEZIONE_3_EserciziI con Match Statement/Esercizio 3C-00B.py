# Esercizio 3C-00B. Scrivere un programma in Python che chieda all'utente 
# di inserire il proprio nome e il proprio genere (specificato con "m" per maschio o "f" per femmina) 
# e utilizzi lo statement match per fornire una risposta adeguata da inserire in un documento di identita'.

# - Se il valore di gender è "m", stampare il nome e il genere come Maschio.
# - Se il valore di gender è "f", stampare il nome e il genere come Femmina.
# - Se il valore di gender è diverso da "m" o "f", stampare un messaggio di errore, 
# indicando che non è possibile generare un documento di identità.


nome: str = input("Inserisci il tuo nome e il tuo genere: ")

genere: str = input("Digitare 'm' per maschio e 'f' per femmina: (m/f)")


match genere:

    case "m":
        print(f"{nome} è Maschio!")
    
    case "f":
        print(f"{nome} è Femmina!")
    
    case _:
        print(f"Mi dispiace {nome}, non e' possibile procedere con la generazione di un documento di identità!")
