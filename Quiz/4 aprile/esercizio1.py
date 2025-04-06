# quiz

# ogni carta ha un valore tra 2 e 11 compresso



# asso = puo valere 1 o 11

# 11 deve avere 1

# (tra 1 e 11)

# se la somma > 21 and asso = 11

def blackjack_hand_total(card: list[int]) -> int:

    somma = 0
    asso = 11

    for i in card:

        if i != asso and somma < 21:
            somma += i

        if somma < 10 and i == asso:
            somma += i

        if somma + 11 > 21:
            somma += 1
        else:
            somma += 11

    
    return somma

     # elif somma < 21 


    

# print(blackjack_hand_total([2, 3, 5]))

# print(blackjack_hand_total([11, 5, 5]))

print(blackjack_hand_total([1, 10, 11]))
       

# esercizio 2

# def find_disappeared_numbers(nums:list[int]) -> list[int]:

#     n =len(nums)

#     lista_mancante = []

#     new_list = nums.copy()
    

#     for numero in range (1, n +1):
#         if numero not in new_list:
#             lista_mancante.append(numero)

#     return lista_mancante


# print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))

# esercizio 3


# def somma_elementi(x: list[int], y: list[int]) -> list[int]:

    

#     for number1 in x:
#         for number2 in y:
#             number1 + number2
             

#         return x + y

new_list = [a + b for a, b in zip(x, y)]
# print(somma_elementi([1,2,-1],[0,-1,0]))

#         if number2 in y:
#             risultato = number1 + number2
#             new_list.append(risultato)
    
#     return x + y


#  for numero in numbers:
#         if numero % 2 == 0:
#             lista_pari.append(numero)
#         elif numero % 2 != 0:
#             lista_dispari.append(numero)
    
#     return lista_pari + lista_dispari



# print(somma_elementi([1,2,-1],[0,-1,0]))
# [1, 1, -1]



