# Esercizi quiz

# Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.

def list_statistics(numbers: list[int]) -> list[int] :

    massimo = max(numbers)

    minimo = min(numbers)

    media = sum(numbers)/len(numbers)

    return massimo, minimo, media


print(list_statistics([1, 1, 1, 1, 2]))

def lis_statistics(numbers: list[int]) ->list[int]:

    massimo = numbers[0]

    minimo = numbers[0]

    somma = 0
    media = 0
   
    for number in numbers:
        if number > massimo:
            massimo = number
        
        elif number < minimo:
            minimo = number

    for number in numbers:
        somma += number
           
    media = somma/len(somma)

    return massimo, minimo, media 

print(list_statistics([1, 1, 1, 1, 2]))







# def list_statistics(numbers: list[int]) -> list[int] :

#     max_numero:int = numbers[0]

#     min_numero:int = numbers[0]

#     somma:int = 0
#     cont_numeri:int = len(numbers)
    
#     media:int = 1

#     for numero in numbers:
#         if numero > max_numero:
#             max_numero = numero
            
#             if numero < min_numero:
#                 min_numero = numero

#         somma = sum(numbers)
#         media = (somma/cont_numeri)


#     return max_numero, min_numero, media


# # print(list_statistics([1, 2, 3, 4, 5]))
# # print(list_statistics([10, 20, 30, 40, 50]))

# # print(list_statistics([-5, -1, -3]))

# print(type(list_statistics([2])))

# print(type(numbers))

# print(list_statistics([1, 1, 1, 1, 2]))



# def list_statistics(numbers: list[int]) -> list[int] :
   
#     max_numero = numbers[0]   # do un valore alla variabile max_numero
#     min_numero = numbers[0]   # do lo stesso valore alla variabile min_numero
#     somma = 0
#     contatore = 1    # contatore delle iterazioni, mi serve per fare la media dei numeri interi
#     media = 0
 
#     for numero in numbers:
#         if numero > max_numero:
#             max_numero = numero
#         if numero < min_numero:
#             min_numero = numero

#         somma += numero
#         media = somma / contatore
#         contatore += 1


#     return max_numero, min_numero, media


#     # cancella ... e definisci il tipo del dato di ritorno, successivamente cancella pass e scrivi il tuo codice
   

# numeri: list[int] = [80,45,345,34,90,23]

# print(list_statistics(numeri))



# # Funzione con il metodo max()

# def numeromax(lista: list[int]) -> list[int]:

#     lista: list[int] = max(lista)

#     lista: list[int] = min(lista)

#     lista: 

# #     return lista




   
