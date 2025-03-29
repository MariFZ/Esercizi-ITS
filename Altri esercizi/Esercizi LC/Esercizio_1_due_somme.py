# Esercizio 1
#  Dato un array di numeri interi nums e un numero intero target, restituisci gli indici dei due numeri in modo che la loro somma sia target .

# Si può supporre che ogni input abbia esattamente una soluzione e non si può utilizzare lo stesso elemento due volte.

# Puoi restituire la risposta in qualsiasi ordine.


def somma(param_1:list[int], parame_2:int = 0) -> list[int]:

    for i in range(len(param_1)):
        for j in range(i + 1, len(param_1)):
            if param_1[i] + param_1[j] == parame_2:
                return i, j

    return []

nums = [2,7,11,15]
target = 9  
print(somma(nums, target))

# numeri = [3,2,4]
# target2 = 6
# print(somma(numeri, target2))


# numeri2 = [3,3]
# target3 = 6
# print(somma(numeri2, target3))

# invece inserito in una classe

# class Solution():






