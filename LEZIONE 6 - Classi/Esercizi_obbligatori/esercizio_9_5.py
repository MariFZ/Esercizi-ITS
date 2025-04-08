# 9-5
# Login Attempts
# Add an attribute called login_attempts to your User class from Exercise 9-3. 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
# Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, 
# and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

# 9-5. Tentativi di accesso
# Aggiungere un attributo chiamato login_attempts alla classe User dell'Esercizio 9-3. 
# Scrivere un metodo chiamato increment_login_attempts( che incrementa di 1 il valore di login_attempts. 
# Scrivete un metodo chiamato increment_login_attempts() che incrementa il valore di login_attempts di 1. 
# Scrivete un altro metodo chiamato reset_login_attempts() che reimposta il valore di login_attempts a 0. 
# Create un'istanza della classe User e chiamate increment_login_attempts() diverse volte. 
# Stampare il valore di login_attempts per assicurarsi che sia stato incrementato correttamente 
# e quindi chiamare reset_login_attempts(). 
# Stampare nuovamente login_attempts per verificare che sia stato riportato a 0.


class User:
    def __init__(self, first_name:str, last_name:str, citta_nascita: str, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.citta_nascita = citta_nascita
        self.login_attempts = 0  # questo valore non deve essere inserito negli argomenti
        self.age = age

    def increment_login_attempts(self) -> int:

        self.login_attempts += 1

    def reset_login_attempts(self) -> int:

        self.login_attempts = 0

    
user1:User = User("Mari", "Figueroa", "Roma", 23)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"L'utente si è collegato: {user1.login_attempts}")

# richiamo la funzione per risettare il valore
user1.reset_login_attempts()
user1.reset_login_attempts()

print(f"L'utente {user1.first_name} - login attemps risettato al valore originale: {user1.login_attempts}")


