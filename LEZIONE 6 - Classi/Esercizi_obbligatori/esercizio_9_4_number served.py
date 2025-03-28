# Esercizio 9-4. 
# Number Served
# Start with your program from Exercise 9-1. 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and then change this value and print it again. 
# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again. 
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business

class Restaurant:

    def __init__(self, nome_ristorante:str, tipo_cucina:str):
        
        self.nome_ristorante = nome_ristorante
        self.tipo_cucina = tipo_cucina
        self.number_served = 0 # inserito qui, perchè un valore di default
        '''Non si mette nella prima riga (come parametro del construttore,)
        perchè la traccia specifica che deve avere un valore predifinito di 0.
        Se lo mettessimo tra i parametri del costruttore, significherebbe che 
        l'utente dovrebbe specificarlo ogni volta che crea un'istanza, il che 
        NON E' RICHIESTO'''

        '''SPIEGAZIONE: 
        Il modo corretto per rispettare la traccia è inizializzare number_served = 0 dentro il costruttore, 
        senza metterlo tra i parametri. In questo modo, ogni ristorante 
        avrà automaticamente il valore iniziale 0 senza che l'utente debba specificarlo. '''

    def describe_restaurant(self):
        print(f"Il nome del ristorante è: {self.nome_ristorante} e il tipo di cucina è: {self.tipo_cucina}")

    def open_restaurant(self):
        print(f"Il ristorante: {self.nome_ristorante} è aperto! :)")
    
    def set_number_served(self, number_served):
        '''Set: mi permette di impostare un valore'''
        self.number_served = number_served

    def increment_number_served(self, altri_clienti):
        '''Creo un paramentro: 
            altro cliente: che rappresenta il numero di clienti aggiuntivi
             che sono stati serviti '''
        self.number_served += altri_clienti
        '''Aumento il valore dell'attributo number_server dell'oggetto.
        self.number_served è l'attributo che tiene traccia del numero di clienti serviti, e con += stai aggiungendo il valore di altro_cliente a number_served.
        In altre parole, se al momento il ristorante ha servito 4 clienti 
        (number_served = 4) e oggi vengono serviti 10 clienti in più, 
        dopo aver chiamato increment_number_served(10), 
        il numero di clienti serviti diventa 14.'''
     

# creo l'istanza chiamata restaurant della classe Restaurant
restaurant:Restaurant = Restaurant("Il Bucco","Cucina cinese")
'''Qui non deveo scrivere il numero assegnato al cliente'''

# chiamo il metodo: describe_restaurant per vedere l'informazione iniziale
restaurant.describe_restaurant()

# Print the number of customers the restaurant has served, 
# and then change this value and print it again.
'''In questa parte della traccia, questo valore lo cambio nel default...0, 10, 14 '''

print(restaurant.number_served)
'''Di questa maniera posso vedere il valore assegnato di default = 0, 15, ecc'''

# modifico il valore di number_server con il metodo: set_number_server
restaurant.set_number_served(4)
'''set__() e il valore dentro, è utile per aggiungere logiche (come validazioni) prima di assegnare un valore.'''
# restaurant.number_served = 8
'''perché stai cercando di assegnare un valore direttamente al metodo e non all'attributo. 
Il metodo è una funzione, non una variabile, 
quindi la sintassi corretta per invocarlo è con le parentesi: restaurant.set_number_served(8).'''

# stampo il valore di number server che ho impostato per l'istanza restaurant dopo la modifica
print(restaurant.number_served)

restaurant.increment_number_served(1000)
print(restaurant.number_served)



