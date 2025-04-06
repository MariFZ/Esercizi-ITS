# Dada una lista de enteros, regresa los índices de los dos números que sumen un valor específico.
'''tecnica de los dos punteros:


Paso 1: Crear dos punteros. Uno al principio de la lista y otro al final
Para nuestro ejemplo el puntero 1 tiene el valor del índice 0 y el puntero 2 el valor del índice 4.

Paso 2: Verificar si la suma de los dos valores es igual a nuestro objetivo

Si la suma de los dos valores es igual al objetivo, entonces encontramos el par y sólo deberíamos devolver sus índices.
Si la suma es mayor, entonces necesitamos una suma menor por lo que vamos a disminuir el puntero 2.
Si la suma es menor, entonces necesitamos una suma mayor por lo que vamos a aumentar el puntero 1.

La única razón por la que aumentamos o disminuimos los punteros nuestra suma aumenta o disminuye es porque la lista está ordenada.

'''

# numeros = [1, 2, 7, 11, 19]
# suma = 9

# p_izquierdo = 0
# # p_derecho = len(numeros) # Esto devuelve 5, porque hay 5 elementos en la lista.  El índice máximo es siempre uno menos que el tamaño de la lista.
# p_derecho = len(numeros) -1 # # Esto es 5 - 1 = 4, por lo que el último elemento está en el índice 4

# suma_parcial = 0

# def dos_sumas(numeros:list[int], suma) -> list:
    
#     p_izquierdo = 0
#     p_derecho = len(numeros) -1
#     suma_parcial = 0

#     while p_izquierdo < p_derecho:
#         suma_parcial = numeros[p_izquierdo] + numeros[p_derecho]
    
#         if suma_parcial == suma:
#             return [p_izquierdo, p_derecho]

#         if suma_parcial  > suma:
#             p_derecho -= 1
    
#         else:
#             p_izquierdo += 1
        
#     return [-1, -1]

# numbers = [1, 2, 7, 11, 19]
# suma = 9

# print(dos_sumas(numbers, suma))


# def dos_sumas(numeros, suma):
#     puntero_izquierdo = 0
#     puntero_derecho = len(numeros) - 1

#     while puntero_izquierdo < puntero_derecho:
#         suma_actual = numeros[puntero_izquierdo] + numeros[puntero_derecho]
    
#         if suma_actual == suma:
#             return [puntero_izquierdo, puntero_derecho]
#         if suma > suma_actual:
#             puntero_izquierdo += 1
#         else:
#             puntero_derecho -= 1
#     return [-1, -1]

# numbers = [1, 2, 7, 11, 19]
# suma = 9

# print(dos_sumas(numbers, suma))


# Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
# Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
# For example:

# Test	Result
# print(count_isolated([1, 2, 2, 3, 3, 3, 4])) ----  2
# print(count_isolated([1, 2, 3, 4, 5])) ----  5

# def count_isolated(lista: list[int]) -> int:

#     isolato = []

#     # controllo il primo numero

#     for i in range(len(lista)):

#         if i ==0:

#             if lista[i] != lista[i +1]:
#                 isolato.append(i)

#         # elif lista[1] != 

#     # controllo l'ultimo

#         elif i == len(lista) -1:
        
#             if lista[i] != lista[i -1]:
#                 isolato.append(i)
        
#         elif i == len(lista) -1:
        
#             if lista[i] != lista[i - 1]:
#                 isolato.append(i)

#     # controllo gli altri

#         else:
#             if lista[i] != lista[i +1] and lista[i] != lista[i -1]:
#                 isolato += 1


#     return len(isolato)



# print(count_isolated([1, 2, 2, 3, 3, 3, 4]))

# n = 5

# # for i in range(n, -1, -1):
# #     print(i)

# for i in range(1,n+1):
#     print(i)

# esercio 9
# primo quiz

# Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.


# def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:

#     new_set = set()

#     for ele in original_set:
#         if ele not in elements_to_remove:
#             new_set.add(ele)

#     return new_set

# set_old = (5, 6, 7)
# lista = [7, 8, 9]

# print(remove_elements(set_old, lista))


# Esercizio 1
# LeetCode
#  Dato un array di numeri interi nums e un numero intero target, restituisci gli indici dei due numeri in modo che la loro somma sia target .

# Si può supporre che ogni input abbia esattamente una soluzione e non si può utilizzare lo stesso elemento due volte.

# Puoi restituire la risposta in qualsiasi ordine.

# def somma(param_1:list[int], parame_2:int = 0) -> list[int]:

    
#     indici = []
#     somma_parziale = 0
#     i = 0
#     while i < len(param_1):
#         somma_parziale = param_1[i] + param_1[i +1]
#         if somma_parziale == parame_2:
#             indici.append(i)
#         i += 1
    
#     return indici


# nums = [2,7,11,15]
# target = 9  
# print(somma(nums, target))


def somma(param_1:list[int], parame_2:int = 0) -> list[int]:

    indici = []

    for i in range(len(param_1)):
        for j in range(i + 1, len(param_1)):
            somma_parziale = param_1[i] +  param_1[j] 
            if somma_parziale == parame_2:
                indici.append(i)
                indici.append(j)


    return indici


nums = [2,7,11,15]
target = 9  
print(somma(nums, target))







