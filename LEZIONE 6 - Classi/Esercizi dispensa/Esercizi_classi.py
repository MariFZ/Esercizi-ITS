# Esercizi classi


class Persona:
    '''super classe Persona che condiziona le altre'''

    def __init__(self, nome, cognome, eta):
        '''Init si denomina: Costruttore perchè crea/inizializza la classe'''

        self.nome = nome
        self.cognome = cognome
        self.eta = eta


alice = Persona("Alice", "Bran", 45)



    
def get_nome(self):

    return self.nome
    
def set_name(self, nome):

    self.nome = nome


class Dipendente(Persona): 
    
    def __init__(self, nome, cognome, eta, stipendio):

        super().__init__(nome, cognome, eta)
        self.stipendio = stipendio
