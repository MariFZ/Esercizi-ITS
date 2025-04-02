# Esercizio per 9.11

class User:
    def __init__(self, nome:str, cognome:str, username:str, email:str):
        self.nome = nome
        self.cognome = cognome
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"Il nome dell'utente è: {self.nome} \nil suo cognome è: {self.cognome}\
            \nil suo username è: {self.username} \ne la sua mail è: {self.email}\n")
    
    def greet_user(self):
        print(f"Ciao {self.nome}! Benvenuto!\n")
    

class Privilegi:
    def __init__(self, lista_privilegi:list =[]):
        self.lista_privilegi = lista_privilegi
    
    def show_privilegi(self):
        for privilegio in self.lista_privilegi:
            print(f"{privilegio}")


class Admin:
    '''Admin: memorizza un'istanza Utente e un'istanza Privilegi come attributi.'''
    def __init__(self, user_instance):   # user_instance sarebbe un'istanza completa della classe User, quindi è chiamato self.user
        self.user = user_instance # 
        self.privilegi = Privilegi()  # va in con P maiuscola perchè si riferisce alla classe che gestisce i privilegi
        




