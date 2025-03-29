# Esercizio 125 
# Palindromo valido

# Una frase è palindroma se, dopo aver convertito tutte le lettere maiuscole in minuscole e rimosso tutti i caratteri non alfanumerici, 
# si legge allo stesso modo avanti e indietro. I caratteri alfanumerici includono lettere e numeri.

# Data una stringa s, restituisci true se è palindroma , false altrimenti .



class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        tolgo_spazi = ""
        non_permesso = [",", ":", ";", "!", " ", ".", "?"]

        for c in s:
            if c not in non_permesso:
                tolgo_spazi += c.lower()
        
              
        return  tolgo_spazi == tolgo_spazi[::-1]


stringa = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(stringa))


