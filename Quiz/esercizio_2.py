# esercizio 2

# Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.

# def remove_duplicates(lista[str]) -> list: [int, str]

def remove_duplicates(lista: list[str, int]) -> list[str, int]:

    new_list:list[int,str] = []

    for elemento in lista:
        if elemento not in new_list:
            new_list.append(elemento)
    
    return new_list


# print(remove_duplicates([1, 2, 3, 1, 2, 4]))
# print(remove_duplicates([4, 5, 'a', 4, 6]))
# print(remove_duplicates(['a', 'b', 'a']))
# print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([]))





























    # elementi: list[str] = []

    # for elemento in lista:
    #     if elemento not in elementi:
    #         elementi.append(elemento)

    # return elementi

# stringa = [1, 2, 3, 1, 2, 4]
# stringa2 = [4, 5, 'a', 4, 6]

# print(remove_duplicates(stringa))
# print(remove_duplicates(stringa2))

