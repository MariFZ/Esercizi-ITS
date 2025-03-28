# esercio 9

# Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.


def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    '''Da ricordare:
        Un set vuoto, in Python,  che si deve riempire tramite "add" con altri elementi
        se deve iniziare cosi:     nomeset:set = set()
        se si fa:                  nomeset:set = {} 
        Python l'interpreta come un dizionario

        Se invece il set contiene degli elementi: torna alla sua struttura:

        * nomeset:set = {0,3}
        '''

    set_nuovo:set = set()
    
    for numero in original_set:
        if numero not in elements_to_remove:
            set_nuovo.add(numero)
    return set_nuovo


# def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:


#     list_new:list = []

#     for numero in original_set:
#         if numero not in elements_to_remove:
#             list_new.append(numero)
    
#     return set(list_new)


# set_old = (5, 6, 7)
# lista = [7, 8, 9]


# print("------------------------------------")

# def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:

#     set_nuovo:set = {}


#     for numero in original_set:
#          if numero not in elements_to_remove:
#             set_nuovo.add(numero)

#     return set_nuovo

# set_old = (5, 6, 7)
# lista = [7, 8, 9]

# print(remove_elements(set_old, lista))


def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    '''Da ricordare:
        Un set vuoto, in Python,  che si deve riempire tramite "add" con altri elementi
        se deve iniziare cosi:     nomeset:set = set()
        se si fa:                  nomeset:set = {} 
        Python l'interpreta come un dizionario

        Se invece il set contiene degli elementi: torna alla sua struttura:

        * nomeset:set = {0,3}
        '''

    set_nuovo:set = set()
    
    for numero in original_set:
        if numero not in elements_to_remove:
            set_nuovo.add(numero)
    return set_nuovo
  


# print(type(remove_elements()))

# print(type(remove_elements({5, 6, 7}, [7, 8, 9])))

print(remove_elements({5, 6, 7}, [7, 8, 9]))

   

# nomeSet = {"John", "Jane", "Doe"}

# nomeSet.add("Ihechikara")

# print(nomeSet)
# # {'John', 'Ihechikara', 'Doe', 'Jane'}