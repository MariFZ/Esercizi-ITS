# funzione countdown

'''ciclo while'''
# def countdown(n:int) -> None:

#     if n >= 0: # cioè se n è positivo
#         while n >= 0:
#             print(n)
#             n -=1
#     else:
#         print("Errore! scrive un numero positivo")


# countdown(-5)

# '''ciclo for'''
# def countdown(n:int) -> None:

#     if n >=0:
#         for i in range(n,-1, -1):
#             print(i)
#     else:
#         print("Errore! Devi scrivere un numero positivo")

# countdown(5)
# print(countdown(5))
# '''non devo fare print perchè la funzione non ha un return e quindi mi stampa None'''


'''funzione ricorsiva'''


# def countdownricorsivo(n:int) -> None:

#     if n < 0:  # per evitare un countdowm di numeri negativi, imposto la condizione di arresto, n < 0 perchè sino stampa numeri negativi finche fa crash
#         return print("Errore")
    
#     if n == 0: # E' importante inserire la condizione di base/ arresto perchè si fermi la ricorsione, nel caso dei numeri positivi, fino va dal numero positivo e va oltre
#         print(0)

#     else:   
#         print(n)
#         countdownricorsivo(n -1)

# countdownricorsivo(5)


# esericizio pag 20

# Write a function called sum that takes a positive integer number n as input and returns the sum of the numbers from 0 to n. 
# If the input number n is negative, display an error message and the function must return 0.
# To implement the sum function, you must exclusively use a while loop and the parameter n passed as input to the function.
# It is allowed to declare only one variable inside the function to manage the sum.
# Then, call the function sum for n = -5 and n = 5.
# Expected Output:
# Error! Inserted number is negative!

# def sum(n:int) -> int:
  
#     if n < 0:
#         print("Errore")
#         return 0
       
#     else:
#         somma = 0
#         while n >=0:
#             somma += n
#             n -= 1
#         return somma 

# # sum(0)

# # sum(-3)

# print(sum(-5))

'''funzione sum ricorsiva'''

# Write a Python function called recursiveSum that, given a n integer n as input, recursively calculates the sum of the numbers from 0 to n.
# If the input number n is negative, display an error message and the function must return 0.
# Then, call the function recursiveSumfor n = -5 and n = 5.

# def sumrecursive(n:int) ->int:

#     if n < 0:
#         print("Errore")
#         return 0
#     elif n == 0:
#         return 0
#     else:
#         return int(n + sumrecursive(n-1)) # scrivendo int trunca/ arrotonda il numero se fosse decimale
    
# print (sumrecursive(5.3))


# esercizio pag 43

# Write a function sumInRange that calculates the sum of all integers between a and b, inclusive, where a and b are passed as input to the function.
# To solve the exercise, it is mandatory to use a while loop, and it is assumed that the value of b is always greater than the value of a. 
# Therefore, if a > b, it is necessary to swap the values to ensure that a is the smaller of the two.
# Finally, it is allowed to declare only one variable, in addition to the function parameters, to store the sum.
# Then, call the function sumInRangefor a= 5, b= 10 and for a= 10, b = 5.


'''ciclo while'''

# def sumInRanget(a:int, b:int) ->int:

#     if a > b: # a= 3, b= 2
#         temp = a  # se i valore di a è più grande, scambio i loro valori, "copiando" il valore di a in un'altra variabile
#         a = b
#         b = temp
    
#     somma = 0
#     while a <= b:
#         somma += b
#         b -= 1
#     return somma
        
# print(sumInRanget(10,5))


'''somma con funzione ricorsiva'''

# Write a recursive function recursiveSumInRange that calculates the sum of all integers between a and b, inclusive, 
# where a and b are passed as input to the function.
# Assume that the value of b is always greater than the value of a. 
# Therefore, if a > b, it is necessary to swap the values to ensure that a is the smaller of the two.
# Then, call the function recursiveSumInRangefor a = 5, b = 10 and for a = 10, b = 5.

# def recursiveSumInRange(a:int, b:int) ->int:

#     if a > b:
#         temp = a
#         a = b
#         b = temp
    
#     elif a == b:
#         return (a)
#     somma = 0
#     while a <= b:
#         somma += b
#         return int(b + recursiveSumInRange(a, b - 1)) 
#     '''fa un countdown 10 + 9 +8 + 7+ 6 + 5 + 4 +3 +2 +1!------   ;) '''
    
# print(recursiveSumInRange(10,10))

# 

# Esercizio 1

# Scrivere in Python una funzione recursivePower che calcola la potenza di un numero utilizzando la ricorsione. 
# La funzione deve ricevere due parametri in input:

# base: il numero da elevare a potenza.
# exponent: l’esponente a cui elevare la base.
# Utilizzare, poi, la funzione per calcolare:

# 3⁴, ovvero 3 elevato alla potenza di 4. 
# 43 , ovvero 4 elevato alla potenza di 3.
# 25, ovvero 2 elevato alla potenza di 5. 
# 52, ovvero 5 elevato alla potenza di 2.

# def potenzanumero(base, exponente): 
#     if exponente == 0:
#         return 1
#     else:
#         return base * potenzanumero(base, exponente -1)

# print(potenzanumero(3,4))

# print(potenzanumero(4,3))

# print(potenzanumero(2,5))

# print(potenzanumero(2,5))

# print(potenzanumero(5,2))

# Esercizio 2.
# Si supponga di voler calcolare l'ammontare del denaro depositato su un conto bancario ad interesse composto. 
# Se m è la somma depositata sul conto, la somma disponibile alla fine del mese sarà 1.005 volte m.
# Scrivere una funzione ricorsiva compoundInterest che calcoli la somma presente sul conto dopo t mesi data una somma di partenza m.

# def compundInterest(m:float, t:float) -> float:
#     '''m è il valore iniziale sul conto. '''
    
#     if t == 0:
#         return m

#     else:
#         return 1005 * compundInterest(m, t - 1) # il calcolo si fa: saldo = m * t(1005)

# print(compundInterest(100, 3))

# Esericio 3

# Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

# n * (n-1) * (n-2) * ... * 1

# con 1! uguale a 1 e 0! definito come 1.
# Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!.

# def recursiveFatorial(n:int) ->int:

#     if n ==0:
#         return 1
#     return n * recursiveFatorial(n -1)

# print(recursiveFatorial(5))

# Esercizio 4

# Scrivere una funzione ricorsiva recursiveDigitCounter che restituisca il numero di cifre di un numero intero n passato in input.
# Sono permessi sia valori positivi che negativi per n.
# Ad esempio, il numero -120 ha 3 cifre.
# Non si tenga conto di eventuali zeri non significativi.

# Suggerimento: per il calcolo delle cifre, fare un controllo se il valore assoluto di n sia minore di 10. 
# In caso positivo, significa che il numero n ha una sola cifra. In caso negativo, significa che il numero n ha più cifre; 
# dunque, dividere n per 10 per rimuovere l'ultima cifra e richiama ricorsivamente la funzione, 
# fino a ottenere un numero con una sola cifra.

# def recursiveDigiCount(n:int) -> int:

#     if n < 10:
#         # print (f"Il numero {n} ha una sola cifra")
#         return  1
        
#     elif n > 10:
#         return 1 + (recursiveDigiCount(n//10))

#     '''cosa ha fatto? ...dopo il secondo controllo giachè più grande di 10, quindi ha come minimo 1 
#     digito, mi serve per fare la somma in avanti....
#     DA RIFARE '''

# print(recursiveDigiCount(12300)) 


# Esercizio 5.

# Una progressione armonica è definita come il prodotto dei reciproci dei primi n numeri interi positivi, 
# ovvero il risultato della moltiplicazione di 1 diviso ogni numero intero da 1 fino a n.
# Ad esempio, se n = 6, la progressione armonica A vale:
# A = 1/6 * 1/5 * 1/4 * 1/3 * 1/2 * 1 = 0.001389.

# Scrivere in Python una funzione ricorsiva chiamata armonica che dato un numero n intero positivo, 
# calcoli la relativa progressione armonica, arrotondando il risultato finale a 6 cifre decimal

# def armonica(n:int) ->float:

#     if n ==1:
#         return 1
    
    
#     else:
#         return 1/n  * armonica(n - 1)

# def calcolaarmonica(n:int) -> float:

#     return round(armonica(n),6)


# print(calcolaarmonica(6))

# Esercizio 6

# Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. Sia Pi una produttoria definita come segue:
# Pi = (0 + 2) * (1 + 2) * (2 + 2) * ... * (n + 2).  

# Calcolare il valore della produttoria Pi se n = 7


# def produttoria(n:int) -> int:

#     # caso base: se n è 0, la produttoria è 1, perchè una produttoria vuota è per definizione
#     if n == 0:
#         return 1
    
#     else:
#         # passo ricorsivo: moltiplichiamo (n+2) con la produttoria di n -1
#        return (n + 2) * produttoria(n - 1)


# n = 7

# print(produttoria(n))

# Esercizio 7

# Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. Sia Pi3 una produttoria definita come segue:
# Pi3 = (1**3) * (2**3) * (3**3) * ... * (n**3)  

# Calcolare il valore della produttoria Pi3 se n = 5.

# def produttoriaPi3(n:int) ->float:

#     if n==1:
#         return 1

#     else:
#         return (n**3) * produttoriaPi3(n -1) 
    
# n = 5

# print(produttoriaPi3(5))

# Esercio 8

# Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

# Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri compresi 
# tra il secondo e l'ultimo della stringa originale.
# L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.

# def vowelsCounter(stringa:str) ->int:

#     # maria

#     if len(stringa) == 0:
#         return 0
    
#     else:
#         vocali = ["a", "e", "i", "o", "u"]
#         lettera = stringa[0]
    
#         if lettera in vocali:

#             return 1 + vowelsCounter(stringa[1:])
        
#         else:
#             return vowelsCounter(stringa[1:])



# def vowelsCounter(stringa:str) ->int:

#     # maria

#     if len(stringa) == 0:
#         return 0
    
#     else:
#         vocali = ["a", "e", "i", "o", "u"]
       

#         if stringa[0] in vocali:
#            return 1 + vowelsCounter(stringa[1:])
        
#         else:
#             return vowelsCounter(stringa[1:])






            
# print(vowelsCounter("maria"))

# def vocali(stringa: str):

#     vocali = ["a", "e", "i", "o", "u"]
#     cont = 0

#     for lettera in stringa:
#         if lettera in vocali:
#             cont += 1
    
#     return cont

# print(vocali("maria"))

    

lista = ['a', 'b', 'c', 'd']
for i in range(len(lista)):  # range(len(lista)) genera i numeri da 0 a 3
    print(lista[i])  # Accediamo agli elementi tramite l'indice

for i in lista:
    print(i)





































# def recursivePower(base, exponent):
#     if exponent == 0:  # Base case
#         return 1
#     else:  # Recursive case
#         return base * recursivePower(base, exponent - 1)

# # Example usage
# print(recursivePower(3, 4))  # Output should be 81


















