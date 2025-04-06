# esercizio 2

# Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, dove n è la lunghezza della lista. 
# Tuttavia, alcuni numeri potrebbero mancare: la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.

# Il tuo compito è individuare i numeri mancanti.

# Scrivi una funzione che, data in input una lista, 
# restituisca una nuova lista ordinata contenente tutti i numeri da 1 a n che non sono presenti nella lista originale.

# def find_disappeared_numbers(nums:list[int]) -> list[int]:

#     new_list:list = []

#     n = len(nums)

#     # for numero in range(1, len(nums) +1)):
#     
#         '''con questo metodo, semplicemente creo una lista ordinata fino alla lunghueza'''
#         new_list.append(numero)

#     return new_list

# print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))



def find_disappeared_numbers(nums:list[int]) -> list[int]:

    new_list:list = []

    n = len(nums)

    # creo una lista (range fa questo) che va da 1 fino alla lunguezza della lista di indici, sempre n +1 
    for numero in range(1, len(nums) + 1):
        '''Lista ordinata contiene numeri senza dupplicati'''
        if numero not in nums:
            '''verifico se il numero NON è presente nella lista "nums", se non è presente l'aggiungo '''
            new_list.append(numero)

    return new_list

# print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))
# print(find_disappeared_numbers([1,8,9,150]))
print(find_disappeared_numbers([1,8,9,150,9,2189,2,82,3,3,3]))

