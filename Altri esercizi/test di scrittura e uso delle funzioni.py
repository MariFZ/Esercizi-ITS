# test di scrittura e uso delle funzioni


frutta: list = ["banana", "pera", "mela" ]
verdura: list= ["spinaci", "zucchine", "melanzane"]

frutta.append("melone")
print(frutta)

print(frutta[3])

frutta.extend(["ciliegia", "mandarino"])
print(frutta)

formaggi: list = ["Gouda", "primo_latte", "gorgonzolla"]
print(formaggi)

lista_frutta_formaggi: list = ([frutta] + [formaggi])
print(lista_frutta_formaggi)
matrice: list = ([2,1], [5,3]) 
img: list = ([0,1,1], [1,0,0], [0,0,0])
print(img)


lista_frutta_formaggi: list = ([*frutta] + [*formaggi])
print(lista_frutta_formaggi)

lista_frutta_formaggi: list = ([*frutta] + [*formaggi])
print(lista_frutta_formaggi)

print(lista_frutta_formaggi[:3])

print(lista_frutta_formaggi[-4])
print(lista_frutta_formaggi[1:2:8])
print(f"Lista della spesa: {lista_frutta_formaggi}")

lista_frutta_formaggi.remove("banana")
lista_frutta_formaggi.append("banana")

print(lista_frutta_formaggi)
lista_frutta_formaggi.remove("banana")
print(lista_frutta_formaggi)

print(f"Lista senza banane: {lista_frutta_formaggi}") # la f qui permette di includere espressioni all'interno delle stringhe racchiudendole tra parentesi graffe

a: list = [1,2,3]
b: list = [4,5,6]

print(a+b) # mette 2 liste insieme

print(f"Funzione Extend: {a}") 
print(a.append(b))   
print(f"Funzione Append:{a}")