# Esercizio 9.13
# Dice
# Make a class Die with one attribute called sides, which has a default value of 6. 
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times

# 9-13. Dadi: create una classe Die con un attributo chiamato sides, che ha un valore predefinito di 6. 
# Scrivete un metodo chiamato roll_die() che stampa un numero casuale compreso tra 1 e il numero di lati del dado. 
# Creare un dado a 6 facce e lanciarlo 10 volte. Creare un dado a 10 facce e un dado a 20 facce. Lanciare ogni dado 10 volte


import  random

class Die:
    def __init__(self, side = 6):

        self.side = side
    
    def roll_die(self):
        
        return random.randint(1, self.side)

dado1 = Die()

dado1.roll_die()

print(dado1.roll_die())

risultati_dado1 = []

for numero in range(10):

    risultati_aleatorio = dado1.roll_die()
    risultati_dado1.append(risultati_aleatorio)

print(f"Questi sono i risultati: {risultati_dado1}")

dado2 = Die(20)
risultati_dado2 = []

for numero in range(10):

    risultati_aleatorio = dado2.roll_die()
    risultati_dado2.append(risultati_aleatorio)

print(f"Questi sono i risultati: {risultati_dado2}")


dado3 = Die(30)

risultati_dado3 = []
for numero in range(10):

    risultati_aleatorio = dado3.roll_die()
    risultati_dado3.append(risultati_aleatorio)

print(f"Questi sono i risultati: {risultati_dado3}")



