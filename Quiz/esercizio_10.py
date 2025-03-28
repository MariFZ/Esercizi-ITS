# esercizio 10

# Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    
    new_dizionario:dict = {}

    # mi creo una copia del dict 1 in dizionario. 
    # Questa è la versione più macchinosa, perche sino potevo fare:
    '''new_dizionario:dict = dict1.copy()'''

    for chiave1, valore1 in dict1.items():
       new_dizionario[chiave1] = valore1

    # prendo chiave/valore del dict2 e vedo se sono nel dizionario
    for chiave2, valore2 in dict2.items():
        if chiave2 in new_dizionario:
            new_dizionario[chiave2] += valore2 # aggiorno il valore 
        else:
            new_dizionario[chiave2] = valore2

    return new_dizionario

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dictionaries({}, {}))

# soluzione copiando il dizionario 1 in new dizionario

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:

    new_dizionario:dict = dict1.copy()

    for chiave, valore in dict2.items():
        if chiave in new_dizionario:
            new_dizionario[chiave] += valore
        else:
            new_dizionario[chiave] = valore

    return new_dizionario

print(merge_dictionaries({}, {'a': 10, 'b': 20}))





