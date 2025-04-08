# Esercizio per 9.11

# Imported Admin: Create a module users.py containing three classes:

# User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
# Privileges: holds a list of privileges and a method show_privileges() to display them.
# Admin: stores a User instance and a Privileges instance as attributes.
# In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, 
# and call describe_user() and show_privileges() to verify everything works correctly.


# 9-11. Admin importato: Creare un modulo users.py contenente tre classi:

# User: memorizza nome_nome, cognome, nome utente ed email; include i metodi describe_user() e greet_user().
# Privilegi: contiene un elenco di privilegi e un metodo show_privilegi() per visualizzarli.
# Admin: memorizza un'istanza di Utente e un'istanza di Privilegi come attributi.
# In un file separato main.py, importate le classi, create un'istanza di User e una di Privileges, passatele ad Admin e chiamate describe_user() e show_privileges() per verificare che tutto funzioni correttamente.




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

    def aggiungoprivilegio(self, privilegio):
        self.lista_privilegi.append(privilegio)
    
    def show_privilegi(self):
        for privilegio in self.lista_privilegi:
            print(f"{privilegio}")


class Admin:
    '''Admin: memorizza un'istanza Utente e un'istanza Privilegi come attributi.'''
    def __init__(self, user, privilegi):   # user_instance sarebbe un'istanza completa della classe User, quindi è chiamato self.user
        self.user = user # 
        self.privilegi = privilegi  # va in con P maiuscola perchè si riferisce alla classe che gestisce i privilegi

    def mostra_info_admin(self):
        print("Admin Info")
        self.user.describe_user()
        self.privilegi.show_privilegi()

# Creiamo un'istanza di User
utente1 = User("Mario", "Rossi", "MarioR", "mario@example.com")

# Creiamo un'istanza di Privileges e aggiungiamo alcuni privilegi

admin = ["Accesso completo", "Modifica Utenti", "Gestione sistemi"]

privilegi_admin = Privilegi(admin)


# Creiamo un'istanza di Admin, passando le istanze di User e Privileges
admin1 = Admin(utente1, privilegi_admin)

# Mostriamo le informazioni dell'Admin
admin1.mostra_info_admin()





