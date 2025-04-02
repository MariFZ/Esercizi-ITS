# Esercizio 9-2. 
# Three Restaurants: 
# Start with your class from Exercise 9-1. 
# Create three different instances from the class, and call describe_restaurant() for each instance.

class Restaurant:

    def __init__(self, nome_ristorante:str, tipo_cucina:str):
        
        self.nome_ristorante = nome_ristorante
        self.tipo_cucina = tipo_cucina

    def describe_restaurant(self):
        print(f"Il nome del ristorante è: {self.nome_ristorante} e il tipo di cucina è: {self.tipo_cucina}")

    def open_restaurant(self):
        print(f"Il ristorante: {self.nome_ristorante} è aperto! :)")


if __name__ == "__main__":
    ristorante1:Restaurant = Restaurant("Papillon", "Braceria")
    ristorante1.describe_restaurant()

    ristorante2:Restaurant = Restaurant("La Pinseria", "Pizzeria")
    ristorante2.describe_restaurant()

    ristorante3:Restaurant = Restaurant("Pasqualotto", "Gelatteria")
    ristorante3.describe_restaurant()
