# ESERCIZIO 4

# La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
# Un errore nell'implementazione porta a risultati inaspettati.

# def calculate_average(numbers: list[int]) -> float:
#     '''L'implementazione ha vari errori per cercare la media dei numeri
    
#         1. La media non si può cercare su una lunguezza che divide per 0
#         2. La somma non dovrebbe essere negativa'''
    
#     if len(numbers) == 0:
#         # in questo caso il return deve essere 0
#         return sum(numbers) / len(numbers)
#     else:
#         return len(numbers) / sum(numbers) - 1
    

# correzione:


def calculate_average(numbers: list[int]) -> float:

    if len(numbers) == 0:
        return print("Non è possibile calcolare un numero divisibile per 0")

    
    elif len(numbers)/ sum(numbers) - 1:
        return print("Non posso calcolare tra i numeri di elementi e la somma")
    
    else: 
        return sum(numbers)/len(numbers)
    
print(calculate_average([1, 2, 3, 4, 5]))
      
# print(calculate_average([]))

# print(calculate_average([10, 20, 30]))
    




































def calculate_average(numbers: list[int]) -> float:
    
    somma = 0
    media = 0

    for numero in numbers:
        somma += numero

        media = somma/len(numbers)

    return media

        




numeri: list[int] = [1, 2, 3, 4, 5]

print(f"Questa è la media dei nuemri che hai inserito: {calculate_average(numeri)}")