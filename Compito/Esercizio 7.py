# Esercizio 7
# Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori interi, 
# calcoli la somma incrociata degli elementi.
# Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c.

lista_a:list[int] = [10, 20, 30]
lista_b:list[int] = [30, 20, 10]
lista_c:list[int] =[]

contatore:int = 0

while contatore < len(lista_a):

    somma = lista_a[contatore] + lista_b[-(contatore + 1)]
    lista_c.append(somma)
    contatore +=1

print(lista_c)

# soluzione prof. col ciclo For

n:int = len(lista_a) # lunghezza della lista a

for i in range(n):
    # aggiungi alla lista c la somma tra l'elemento i-esimo della lista a e l'elemento (n-1)-i della lista b
    lista_c.append(lista_a[i] + lista_b[(n-1)-i])
    print(lista_c)
    
    '''
    (n-1) -i scorre gli indici in modo decrecente

    1. Sappiamo che la lista è lunga di 3
    2. (n-1) = (3-1) 
        Ad ogni iterazione farà così
        (n-1) - i 

        (n-1) - i =  2 - 0 = 2 -> indice[2]
        (n-1) - 1 =  2 - 1 = 1 -> indice[1]
        (n-1) - 1 =  2 - 2 = 0 -> indice[0]

    '''
    
















# # non ho capito praticamente NIENTE :((
# lunghuezza = int(input("Scrivere la lunghuezza delle delle liste: "))

# lista_a: list[int] = []
# lista_b: list[int] = []
# somma_incrocciata = 0
# lista_c: list[int] = []


# while True:
    
#     if len(lista_a) < lunghuezza:
    
#         number_a=  int(input("Scrive il numero da inserire nella lista a: "))
#         lista_a.append(number_a)
    
#         number_b=  int(input("Scrive il numero da inserire nella lista b: "))
#         lista_b.append(number_b)

#         lista_c = lista_a + lista_b

#         somma_incrocciata += int(number_a + number_b)
#     else:
#         print(f"Gli elementi della \"lista_a \" sono: \n {lista_a} \nGli elementi della \"lista b\" sono: \n{lista_b}, \nGli elementi della \"list_c\"  sono: \n{lista_c} \ne la \"somma incrocciata\" della \"lista a e la lista b\" è: \n{somma_incrocciata}")
#         break
   
 





