# ESERCIZIO 1 - FUNCTIONS

# 1. METTODO PER SOMMARE VARI NUMERI

# Ciclo For

# Sommare i numeri da 1 a 11
# Inizializzo la variabile somma che entrerà nel ciclo e sommerà i numeri

somma_1 = 0     

# Imposto il ciclo For:

for number in range(1,11):
    somma_1 +=number

print(f" Questa è la somma: {somma_1}")

# Sommare i numeri da 20, 38
somma_2 = 0
for number in range(20,38):
    somma_2 +=number
print(f"Questa è la {somma_2}")


# 2. METODO IMPOSTANDO UNA FUNZIONE

# Definisco la funzione e i parametri

def sum(a:int, b:int):

# Imposto la variabile che accoglierà la somma, in questo caso ha il nome result
    somma:int = 0
    for number in range(a, b+1):
        somma += number
    return somma

# nella variabile  mysum, richiamo la funzione sum che ho creato e all'interno scrivo i valori 
# che vanno a sostituire i valori di "a" e "b" nella definzione della funzione
mysum = sum(1, 10)

sum(1,10)

print(sum(1,10))

# ESEMPIO CON LA SOMMA DEI NUMERI TRA [1, 10], [20,38], [35,49]


# definisco la funzione
def somma_numeri(a:int, b:int) -> int:

    somma: int = 0
    for number in range(a, b+1):
        somma += number
        number +=1
    return somma

# richiamo la funzione

somma_3 = somma_numeri(1,10)
somma_4 = somma_numeri(20,38)
somma_5 = somma_numeri(35,49)

print(f"La somma dei diversi risultati è: \nda 1 a 10 è: {somma_3}, \nla somma da 20 a 38 è: {somma_4} \ne la somma tra 35 e 49 è: {somma_5}")



def sum(a:int, b:int) -> int:

    result:int = 0
    for i in range(a, b+1):
        result = result + i
    return result


mysum = sum(1, 10)

sum(1,10)

print(sum(1,10))

# ESEMPIO DI FUNZIONE CON LA SOTRAZIONE

# definisco la funzione

def subtract(a:int, b:int)  -> int: # con questo definisco i dati in interi

    sotrazione: int = a - b          
    return sotrazione

# creo una variabile con contiene i dati che voglio restare

resta = subtract(4, 1)

print(f"La sotrazione dei numeri che hai inserito 4 e 1 è: {resta}")

