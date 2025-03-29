# Esercizio 234 - Lista concatenata palindroma

# Dato il valore head di un elenco concatenato singolarmente, restituisci true se è un palindromoo false altrimenti

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution: 
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
   
        new_list:list = []
    
        # Passo 1: Trasformare la lista concatenata in un array
        while head: 
            new_list.append(head.val)
            head = head.next

        return new_list == new_list[::-1]
    
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(2)
# n4 = ListNode(1)

# n1.next = n2
# n2.next = n3
# n3.next = n4

# sol = Solution()
# print(sol.isPalindrome(n1))


n4 = ListNode(1)
n5 = ListNode(2)

n4.next = n5
sol = Solution()
print(sol.isPalindrome(n4))