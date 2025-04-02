# 9-1. Restaurant: 
# Make a class called Restaurant. 

# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:

    def __init__(self, nome_ristorante:str, tipo_cucina:str):
        
        self.nome_ristorante = nome_ristorante
        self.tipo_cucina = tipo_cucina

    def describe_restaurant(self):
        print(f"Il nome del ristorante è: {self.nome_ristorante} e il tipo di cucina è: {self.tipo_cucina}")

    def open_restaurant(self):
        print(f"Il ristorante: {self.nome_ristorante} è aperto! :)")


restaurante1:Restaurant = Restaurant("Lele", "Hamburgueria")
'''Creo l'istanza della classe Restaurant, 
cioè l'oggetto creato con questa espressione'''


# Stampo individualmente
print(restaurante1.nome_ristorante)
print(restaurante1.tipo_cucina)
        
restaurante1.describe_restaurant()
restaurante1.open_restaurant()
