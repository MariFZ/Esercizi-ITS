# esercizio 8

# Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
# Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
# For example:

# Test	Result
# print(count_isolated([1, 2, 2, 3, 3, 3, 4])) ----  2
# print(count_isolated([1, 2, 3, 4, 5])) ----  5

# def count_isolated(lista: list[int]) -> int:

#     numeri_isolati:list = []

#     for i in range (len(lista)):
#         # scorro la lista una sola volta
#         '''da l'indice 0 alla lunguezza'''

# #  da sinitra: da 0 or il prox. numero! i + 1 -------------
#         if (i == 0 or lista[i] != lista[i -1]) and (i == len(lista)-1 or lista[i] != lista[i + 1]):
#             numeri_isolati.append(i)

#     return len(numeri_isolati)


# lista1 = [1, 2, 2, 3, 3, 3, 4]
# print(count_isolated(lista1))





def count_isolated(lista: list[int]) -> int:

    # Inizializza il contatore per gli elementi isolati
    contatore_isolati = 0
    
    # Itera attraverso la lista
    for i in range(len(lista)):
        # Per il primo elemento, confronta solo con il vicino a destra
      
        if i == 0:
            '''Qui sto dichiarando che il valore di i è uguale a 0'''
           

            if lista[i] != lista[i + 1]:
                '''se il numero all'indice 0 è diverso al numero nell'indice 0 +1,
                    aggiungelo al contatore'''
                contatore_isolati += 1

   
        # Se siamo all'ultimo elemento della lista, confronta solo con il vicino a sinistra
        elif i == len(lista) - 1:
            '''Dichiaro 'i' con l'ultimo elemento della lista'''
            if lista[i] != lista[i - 1]:
                '''confrontiamo solo con l'indice a sinistra ( i-1).'''
                contatore_isolati += 1

        # Per gli altri elementi, confronta sia con il vicino a sinistra che con quello a destra
        else:
            if lista[i] != lista[i + 1] and lista[i] != lista[i - 1]:
                contatore_isolati += 1
    
    return contatore_isolati

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))

# # # Spiegazione passo a passo con il primo esempio:

# Passo 1:
'''Inizializzo le variabili: La lista e il contatore degli elementi isolati'''


# def conta_elementi(lista:list[int]) -> int:

# # lista = [1, 2, 2, 3, 3, 3, 4]
#     contatore_isolati = 0

# # Passo 2:
#     '''Ora itero attraverso gli 'indici' della lista usando un ciclo:
#       'for in range', 
#         facendo 2 eccessioni per i valori che sono agli estremi:''' 

#     for i in range(len(lista)): 

#     # Iterazione 1: solo il primo valore a sinistra
#         '''Assegno a 'i' il valore di 0. (i = 0) - Il primo elemento è 1(indice 0).
#         Questo è il primo elemento della lista, quindi dobbiamo solo confrontarlo con il vicino a destra, che è 2'''

#         if i == 0:
#             if lista[i] != lista[i + 1]:
#                 '''(i= 1), quindi 1 è diverso da (i +1 )=  2, quindi l'elemento è isolato, quindi incrementiamo il contatore:'''
#                 contatore_isolati += 1

#         # Iterazione 2 - per l'ultimo valore a destra
#             '''Do a 'i' il valore dell'ultimo elemento della lista'''

#         elif i == len(lista) -1:
#             if lista[i] != lista[i -1]:
#                 '''(i= 4), quindi 4 è diverso da [i -1], (i=3), incremento il contatore'''
#                 contatore_isolati += 1

#     # Per le altre iterazioni

#         else:
#             if lista[i] != lista[i -1] and lista[i] != lista[i +1]:
#             # if lista[i] != lista[i +1] and lista[i] != lista[i -1]:
#                 contatore_isolati +=1
    
#     return contatore_isolati

# print(conta_elementi([1, 2, 2, 3, 3, 3, 4]))





























