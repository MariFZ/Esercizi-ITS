# Esercizio 680
'''non l'ho capito ancora del tutto ;('''

# Data una stringa s, restituisce true se spuò essere palindroma dopo aver eliminato al massimo un carattere da essa

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
        return True






























# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         def is_palindrome(sub: str) -> bool:
#             return sub == sub[::-1] # controlla se la stringa è palindroma
#             '''Soluzione che segue il concetto Two Pointers'''

#         left = 0 
#         right = len(s) - 1
        
#         while left < right:
#             if s[left] != s[right]:  # Se troviamo un errore (caratteri diversi)
#                 # Prova a eliminare un carattere a sinistra o a destra e controlla
#                 return is_palindrome(s[left + 1:right + 1]) or is_palindrome(s[left:right])
#             left += 1
#             right -= 1
        
#         return True  # Se non ci sono problemi, è già un palindromo    


# stringa1 = "abca"

# sol = Solution()
# print(sol.validPalindrome(stringa1))



# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         def is_palindrome(sub: str) -> bool:
#             return sub == sub[::-1]  # Controlla se una stringa è palindroma
        
        # left, right = 0, len(s) - 1
        
        # while left < right:
        #     if s[left] != s[right]:  # Se troviamo caratteri diversi...
        #         print(f"Lettera sbagliata trovata: {s[left]} (posizione {left}) e {s[right]} (posizione {right})")
                
        #         left_removed = s[left + 1:right + 1]  # Ignora carattere sinistro
        #         right_removed = s[left:right]        # Ignora carattere destro

        #         print(f"Proviamo a ignorare '{s[left]}' → {left_removed}")
        #         print(f"Proviamo a ignorare '{s[right]}' → {right_removed}")

        #         return is_palindrome(left_removed) or is_palindrome(right_removed)

        #     left += 1
        #     right -= 1
        
        # return True  # Se non troviamo errori, è già palindromo

# # Test
# sol = Solution()
# print(sol.validPalindrome("abca"))  # Output: True


