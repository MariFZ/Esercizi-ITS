class Persona:
    '''Il metodo __init__è il costruttore della classe: Viene eseguito automaticamente quando si crea un'istanza di Persona.

     Inizializza tre attributi con valori predefiniti:
     Significa che quando creiamo un oggetto Persona, 
     inizialmente avrà nome e cognome vuoti e l'età pari a 0.'''
     

    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0

        '''sotto spiegazione dell'uso dei valori predefiniti'''

     # metodo displayData: mostra i dati della persona stampandoli a schermo
    def displayData(self) -> None:
            print(f"Nome:{self.name}\nCognome: {self.lastname}\nEta': {self.age}")
    
    # metodo set: mi consente di impostare un valore per self.name
    '''Serve per modificare il nome della persona dopo che l'oggetto è stato creato'''
    def setName(self, name:str) -> None:
         self.name = name

    def setLastname(self, lastname: str) -> None:
         self.lastname = lastname

    def setAge(self, age: int) -> None:
        if age < 0 or age > 150:
            self.age = age
        else:
            self.age = age 

    def getName(self) -> str:
         return self.name
    
    def getLastname(self) -> str:
         return self.lastname
    
    def getAge(self) -> int:
         return self.age
         

# crea un oggetto di tipo Persona
m:Persona = Persona()

# stampa i dati della Persona creata
m.displayData()

# # imposta il nome di una persona
m.setName("Mari")

# imposta il cognome di una persona
m.setLastname("Figueroa")

# impostare l'eta
m.setAge(-29)

m.setAge(29)

m.displayData()
print("-----------------------")
print(m.getName(), m.getLastname(), m.getAge())

# uso dei valori predefiniti

'''con i valori predefiniti nel costruttore, puoi creare oggetti anche senza passare parametri.
Se l'oggetto necessita solo di un valore in un secondo momento (magari tramite un metodo come setName(), setAge()),
'i valori predefiniti ti permettono di farlo senza errori.

Ad esempio, potresti voler creare un oggetto di una persona prima di raccogliere tutti i suoi dati

Un valore predefinito è usato, per inizializzare un contatore a 0

class Persona:
    def __init__(self, name: str, lastname: str = "", age: int = 0):
        self.name = name
        self.lastname = lastname
        self.age = age

p1 = Persona("Mario")  # Il cognome e l'età sono predefiniti
p2 = Persona("Anna", "Rossi", 25)

print(p1.name, p1.lastname, p1.age)  # Mario, , 0
print(p2.name, p2.lastname, p2.age)  # Anna, Rossi, 25

'''

