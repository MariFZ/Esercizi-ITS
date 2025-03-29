# Esercizio 167
# Dato un array di interi indicizzato 1numbers che è già ordinato in ordine non decrescente , \
# trova due numeri tali che la loro somma dia un target numero specifico. Siano questi due numeri e dove .numbers[index1]numbers[index2]1 <= index1 < index2 <= numbers.length

# Restituisce gli indici dei due numeri e sommati di uno come array di numeri interi di lunghezza 2.index1index2[index1, index2]

# I test vengono generati in modo che ci sia esattamente una soluzione . Non puoi usare lo stesso elemento due volte.

# La tua soluzione deve utilizzare solo spazio extra costante.

def twoSum(numbers:list[int], target:int) -> list[int]:

    
    for i in range(len(numbers)):
        for j in range(i + 1, (len(numbers))):
            if numbers[i] + numbers[j] == target:
               return i +1, j + 1
            # l'esercizio è uguale all'altro....semplicemente dovevo alla fine aumentare con 1 \
            # il risultato dell'indice :( mmmm


    return []

numeri = [2,7,11,15]
target = 9


print(twoSum(numeri, target))

numeri = [2,3,4]
target = 6

print(twoSum(numeri, target))


