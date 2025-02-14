print("Hello, World!")
lista_1: list = [1,2,3,4,5] # ATTENZIONE: dichiarare che tipo è la variabile in questo caso : list
lista_1.append(6)
print(lista_1) # le immagini sono rappresentate con le liste

matrice: list = ([2,1], [5,3]) 
img: list = ([0,1,1], [1,0,0], [0,0,0])
print(img)
R: list= ([24, 128, 233], [10,23,255], [1,0.34]) # per rappresentare immagini a colori con la gamma di colore rosso
G: list= ([24, 128, 233], [10,23,255], [1,0.34]) # per rappresentare immagini a colori con la gamma di colore green
B: list= ([24, 128, 233], [10,23,255], [1,0.34]) # per rappresentare immagini a colori con la gamma di colore blue
# nella lista B ho 3 indici 

print(B[0:len(B)]) # mi mostra la lunguezza dei 3 elementi dentro la lista, TUTTI gli INDICI
print(len(B[0])) # mi mostra la lunguezza de primo elemento, il primo indice (una lista) della lista B 

'''B[0] = "Ciao" # qui sto dicendo che all'indice zero lo cambio per la parola Ciao'''

B[0].append("Ciao")
print(B[0]) # qui inserisce la parola Ciao alla lista con al primo indice: [24,128,233, Ciao]

a: list = [1,2,3]
b: list = [4,5,6]

print(a+b) # mette 2 liste insieme

print(f"Funzione Extend: {a}") # la f qui permette di includere espressioni all'interno delle stringhe racchiudendole tra parentesi graffe
print(a.append(b))   
print(f"Funzione Append:{a}")

a: str = "Mari"
str_1: str = f"Funzione Extend: {a}, {a}, {a}" # funzione parentesi grafa
print(str_1)