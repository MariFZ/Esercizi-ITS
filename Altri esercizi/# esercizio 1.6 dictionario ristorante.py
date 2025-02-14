# esercizio 1.6

menu: dict = {"Pizza": 9.0, "Pasta": 10.50, "Zuppa": 7.0, "Hamburger": 15.50, "Cotoletta": 10.00, "Salmone": 20.20, "Patatine fritte": 5.50,"Patate al forno": 5.50, "Verdura del giorno": 7.00, "Cheesecake": 6.00, "Tiramisu": 6.00, "Focaccia con Nutella": 6.00, "Coca Cola": 3.50, "Acqua": 1.50, "Vino": 5.0}

ordine: dict = {"Primo": "Pasta", "Secondo": "Hamburger", "Contorno":"Verdura del giorno", "Bevanda": "Coca Cola", "Dolce": "Cheesecake"}

# PRIMA SOLUZIONE CREANDO UNA VARIABLE VUOTA = TOTALE

totale = 0.0
for piatti in ordine.values():
    totale += menu[piatti]

print(f"Totale: {totale}")

# SECONDA SOLUZIONE USANDO LA FUZNIONE SUM

conto = sum(menu[item] for item in ordine.values())
print(f"Il totale del conto è: {conto}€")


# SOLUZIONE SE VOLESSE AVERE IL VALORE DI TUTTO IL MENU

conto_totale =sum(ordine.values())
print(f"Conto da pagare = {conto_totale}")



