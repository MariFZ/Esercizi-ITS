# esercizio 3

# def somma_elementi(x: list[int], y: list[int]) -> list[int]:

   
#     for number1 in x:
#         for number 2 in y:
#             if number1 in y:
          
#            new_list.append(number1 + number1)
    
#     return new_list

# # print(somma_elementi([1,1,1],[1,1,1]))

	
# print(somma_elementi([1,2,-1],[0,-1,0]))

# def even_odd_pattern(numbers:list[int]) -> list[int]:


#     lista_pari = []
#     lista_dispari = []


#     for numero in numbers:
#         if numero % 2 == 0:
#             lista_pari.append(numero)
#         elif numero % 2 != 0:
#             lista_dispari.append(numero)
    
#     return lista_pari + lista_dispari

# print(even_odd_pattern([3, 6, 1, 8, 4, 7]))


# pari = [numero for numero in lista if numero % 2 == 0]   # Filtra i numeri pari
# dispari = [numero for numero in lista if numero % 2 != 0]  # Filtra i numeri dispari
#     return pari + dispari  # Combina le due liste, i pari vengono prima


# esercizio 3


def somma_elementi(x: list[int], y: list[int]) -> list[int]:

    new_list = []
    risultato = 0

    
    for i in range(len(x)):
        for j in range(len(y)): 
            risultato = x[i] + y[i]
        new_list.append(risultato)
             
    return new_list

# for i in range(min(len(x),len(y)))
	
# print(somma_elementi([1,1,1],[1,1,1]))  # 2, 2, 2
print(somma_elementi([1,5],[1,2])) # [2, 7]
# print(somma_elementi([1,2,-1],[0,-1,0])) # [1, 1, -1]
	
# print(somma_elementi([1,5],[1,2]))
	
# print(somma_elementi([-10,-2],[10,8])) # [0, 6]
# print(somma_elementi([-18,2,4,5,1,10,12,45,-1,0,45,0,0,0],[-18,92,91,0,12,-1,48,53,0,0,0,0,-1,7])) # [-36, 94, 95, 5, 13, 9, 60, 98, -1, 0, 45, 0, -1, 7]




# print(somma_elementi([1,2,-1],[0,-1,0]))
	
# print(somma_elementi([1,5],[1,2]))

# [1, 1, -1]


# new_list = [a + b for a, b in zip(x, y)]










