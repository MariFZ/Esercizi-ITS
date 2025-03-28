# Esercizio 9-3. 
# Users: 
# Make a class called User. Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user. 
# Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name:str, last_name:str, citta_nascita: str, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.citta_nascita = citta_nascita
        self.age = age

    def describe_user(self):
        print(f"Il nome dell'utente è: {self.first_name} \nil suo cognome è: {self.last_name}\
            \nla sua città di nascita è: {self.citta_nascita} \ne la sua eta: {self.age}\n")
    
    def greet_user(self):
        print(f"Ciao {self.first_name}! Benvenuto a bordo!\n")

mari:User = User("Mari", "Brand", "Germania", 23)
mari.describe_user()
mari.greet_user()

pauli:User = User("Paulina", "Rossi", "Milano", 34)
pauli.describe_user()
pauli.greet_user()






