# esercizio 3

# Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
# La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.

def somma_elementi(x: list[int], y: list[int]) -> list[int]:

    new_list:list = []

    n = len(x)
    somma = 0

    for number in range (n):
        somma = x[number] + y[number]
        new_list.append(somma)

    return new_list

# print(somma_elementi([1,1,1],[1,1,1]))
print(somma_elementi([-18,2,4,5,1,10,12,45,-1,0,45,0,0,0],[-18,92,91,0,12,-1,48,53,0,0,0,0,-1,7]))

# def somma_elementi(x: list[int], y: list[int]) -> list[int]:

#     new_list:list = []
#     n = len(x)
#     i = 0
#     somma = 0

#     while i < n:
#         somma =  x[i] + y[i]
#         new_list.append(somma)
#         i += 1

    # return new_list

# print(somma_elementi([1,1,1],[1,1,1]))
	
# print(somma_elementi([1,2,-1],[0,-1,0]))

# print(somma_elementi([1,5],[1,2]))

# print(somma_elementi([-18,2,4,5,1,10,12,45,-1,0,45,0,0,0],[-18,92,91,0,12,-1,48,53,0,0,0,0,-1,7]))


