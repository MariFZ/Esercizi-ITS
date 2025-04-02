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

# countdown(-5)
# # print(countdown(5))
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

def recursiveFatorial(n:int) ->int:

    if n ==0:
        return 1
    return n * recursiveFatorial(n -1)

print(recursiveFatorial(5))










































# def recursivePower(base, exponent):
#     if exponent == 0:  # Base case
#         return 1
#     else:  # Recursive case
#         return base * recursivePower(base, exponent - 1)

# # Example usage
# print(recursivePower(3, 4))  # Output should be 81


















