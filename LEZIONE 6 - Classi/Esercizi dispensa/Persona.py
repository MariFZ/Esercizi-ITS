class Persona:
    '''
    Di una persona dobbiamo sapere delle informazioni.
    Queste informazioni vengono chiamate attributi (della classe Persona)

    Quali sono?
    * nome 
    * cognome
    * eta
    
    come li rappresento in Python?

    self.name: str (attributo di tipo stringa)
    self.cognome: str (attributo di tipo stringa)
    self.age: int (attributo di tipo intero)

    '''

    # costruttore delle classe Persona

    def __init__(self, name:str, lastname:str, age:int):

        self.name = name
        self.lastname = lastname
        self.age = age

    # funzione che mostri in output tutti i dati di una persona
    def displayData(self) -> None:
            print(f"Nome:{self.name}\nCognome: {self.lastname}\nEta': {self.age}")


# chiamo la variabile di tipo persona: 
'''scrivo il nome della variabile con due punti e dopo uguale Persona'''

m:Persona = Persona("Tati", "Figueroa", 34 )

print(m)

# mostra i dati di una persona

m.displayData()

# class pag 31

class Person:
    personCount = 0

    def __init__(self, name):
          self.name = name
          self.update()

    @classmethod
    def update(cls):  # per accedere agli attributi di classe
        cls.personCount += 1

alice = Person("Alice")
bob = Person("Bob")
print(Person.personCount)





