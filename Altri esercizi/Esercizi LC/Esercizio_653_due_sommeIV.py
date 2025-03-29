# Esercizio 653

# Dato rootun albero binario di ricerca e un intero k, restituisci true se esistono due elementi nel BST tali che la loro somma è uguale ak, 
# altrimenti .false

from typing import Optional

# class Solution:
def findTarget(root: Optional[list], k: int) -> bool:


    for number1 in range(len(root)):
        for number2 in range (number1 + 1, len(root)):
            if root[number1] + root[number2] == k:
                return True
        else:
            return False



radice = [5,3,6,2,4,0,7]
k = 9   
print(findTarget(radice, k)) # True

radice = [5,3,6,2,4,0,7] # False
k = 28
print(findTarget(radice, k))