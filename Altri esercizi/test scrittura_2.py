# voglio capire un esercizio

a: list = [1,2,3]
b: list = [4,5,6]
a.append(b)
print(a)
print(a[3][0]) # da risultato 4
a: list = [1,2,3]

a.append(b)
'''print(a[0][0]) # i numeri interi non sono indicizzati'''

a.append(b)
print(a[3][0])

frutta: list = ["banana", "pera", "mela" ]
verdura: list= ["spinaci", "zucchine", "melanzane"]
frutta.append(verdura)
print(frutta)
print(frutta[3][2]) # ATTENZIONE: leggere sotto:
'''
il Nò 3 [3] entra nella lista [spinaci...] 
e quindi da lì in avanti inizia il conto...0,1,2 
per questo motivo [3][0] va a prendere la parola melanzane, contando il 
numero 3 da melanzane e dopo va avanti
'''

