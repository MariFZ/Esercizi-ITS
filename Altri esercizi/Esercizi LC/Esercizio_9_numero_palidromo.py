# Esercizio 9

# Dato un intero x, restituisci true se x è un palindromo, e false altrimenti

def palidromo(x:int) -> bool:

    stringa = str(x)

    if stringa == stringa[::-1]:
        return True
    return False

x = 121

print(palidromo(x))


# x = 10
# print(palidromo(x))

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

# uso di [::-1] - [0::] - [1::]

lista = [0, 1, 2, 3, 4]
print(lista[0::]) # [0, 1, 2, 3, 4]
print(lista[::-1])  # [4, 3, 2, 1, 0]  (inverte la lista)
print(lista[1::])   # [1, 2, 3, 4]  (toglie il primo elemento)


