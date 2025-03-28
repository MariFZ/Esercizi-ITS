# ESERCIZIO 2 - FUNCTIONS

# La funzione può restituire più di un valore, usando tuple, dizionari e liste. Il metodo più comune è restituire tuple

#  Esempio:

# definire una funzione che ritorna multipli valori:

# def operations(a:int, b:int) -> tuple[int,int]:

#     somma:int = a + b
#     differenza: int = a - b
#     return somma, differenza

# # creo due variabili che prenderanno il valore delle operazioni

# risultato_somma, risultato_differenza = operations(10,5)

# print(f"Questo è il risultato della somma: {risultato_somma}, e questo è il risultato della differenza: {risultato_differenza}\nvolendo posso fare anche cosi: Questo è il valore della somma e la differenza: {operations(10,5)}")

# ESEMPIO DISPENSA

# define a function returning multiple values(returning a tuple)
    
def operations(a: int, b: int) -> tuple[int, int]:
    
    sum_result:int = a + b
    diff_result:int = a - b

# Returns a tuple with two values
    return sum_result, diff_result

# Assigns values to two variables

print(f"questa è la tupla: {operations(10,5)}")

sum_value, diff_value = operations(10, 5)
print(f" Questo è il valore del risultato della somma nella variabile col nome \"sum_value\": {sum_value}") # Output: Sum: 15
print("Difference:", diff_value)






