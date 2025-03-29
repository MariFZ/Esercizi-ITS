#  Esercizio 1
# Scrivere un programma che permetta all'utente di inserire una serie di parole in input, 
# terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
# Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.


parola: str= "fine"

while True:
    word: str = input("Scrivi una parola per verificare se ha la stessa lettera all'inizio e alla fine: ").lower()  

    if word == parola:
        print(f"Hai inserito {parola} e quindi l'inserimento è concluso") 
        break

    elif word != parola:
        if word[0] == word[-1]:
            print(f"La prima e l'ultima lettera della parola: \"{word}\" sono le stesse")
        else:
            print(f"La prima e l'ultima lettera della parola: \"{word}\" non sono le stesse")

# Attenzione! 
# Un numero/parola palindroma è quella che si scrive uguale "al derecho y al reves"
# roma / amor
# Questo esercizio è diverso quello fatto per il compito, dove si cercava se una parola aveva
# la prima e l'ultima lettera uguali

'''
Quando usare word[0] == word[-1] e quando stringa == stringa[::-1]?
✔ Usa word[0] == word[-1] quando vuoi controllare solo il primo e ultimo carattere di una parola.
✔ Usa stringa == stringa[::-1] quando vuoi verificare se tutta la parola o numero è palindromo.

'''