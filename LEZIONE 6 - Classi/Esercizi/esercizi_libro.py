# Esercizi classi : libro

# Esercizio Libro pag 158
'''creare una classe per i cani'''

class Dog: # Per convenzione, i nomi in maiuscolo si riferiscono alle classi in Python
    '''Non ci sono parentesi nella definizione della classe perché stiamo
                creando questa classe da zero'''

# Una funzione che fa parte di una classe è un metodo
    def __init__(self, name: str, age:str):  
        ''' init è un metodo speciale che Python esegue automaticamente 
        ogni volta che si crea una nuova istanza basata sulla classe Dog.'''
        '''Inizializzo gli attributi name ed eta'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulare il sedersi di un cane in risposta a un comando'''
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulare che si arrotola in risposta ad un commando"""
        print(f"{self.name} is roll over!")

my_dog:Dog = Dog("Bender", 10)

print(f"Il mio cane si chiama: {my_dog.name} e ha {my_dog.age}")  # Per accedere agli attributi di un'istanza, si usa la notazione a punti
'''In questo caso, chiamo l'instanza self.name e self.age(dove self rappresenta la variabile personale che ho creato), in altre parole:
''''Questo attributo my_dog.name si riferisce come self.name nella classe Dog'''

# Chiamare i metodi:
'''Dopo aver creato un'istanza della classe Dog, possiamo usare la notazione a punti per
chiamare qualsiasi metodo definito in Dog. Facciamo in modo che il nostro cane si sieda e si rotoli'''

# Per chiamare un metodo, dare il nome dell'istanza (in questo caso, my_dog) e il metodo che si vuole chiamare, separati da un punto

my_dog.sit() # my_dog è la istanza e sit è il metodo
my_dog.roll_over()

# Creare multiple istanze
'''È possibile creare tutte le istanze(variabili) di una classe di cui si ha bisogno. 
Creiamo un secondo cane (istanza/variabile), chiamato il_tuo_cane'''

my_dog = Dog('Bender', 10)
your_dog = Dog('Zorro', 3)

print(f"Il nome del mio cane è {my_dog.name}.")

print(f"Mio cane ha  {my_dog.age} anni.")

my_dog.sit() # Il mio cane si siede

print(f"\nIl cane della mia sorella è: {your_dog.name}.")
print(f"L'età del cane della mia sorella è: {your_dog.age}")
your_dog.sit() # Pure il cane di mia sorella si siede



