# ESERCIZIO 5
# Verifica se un numero è primo. Progetta un algoritmo per determinare 
# se un numero intero positivo inserito dall'utente è un numero primo.

number =int(input("Inserisci un numero: "))

primo = True

# primo = False

if number < 2:
    print("Il numero non è primo")
else: 
    div = 2
    while div < number:
        if (number % div == 0):
            print("Il numero non è primo")
            primo = False
            break
            
        div += 1
if primo:
    print("Il numero è primo")