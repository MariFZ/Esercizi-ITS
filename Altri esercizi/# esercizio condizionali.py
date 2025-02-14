# esercizio 1.6

menu_ristorante: dict = {"Pizza": 9.0, "Pasta": 10.50, "Zuppa": 7.0, "Hamburger": 15.50, "Cotoletta": 10.00, "Salmone": 20.20, "Patatine fritte": 5.50,"Patate al forno": 5.50, "Verdura del giorno": 7.00, "Cheesecake": 6.00, "Tiramisu": 6.00, "Focaccia con Nutella": 6.00, "Coca Cola": 3.50, "Acqua": 1.50, "Vino": 5.0}

# Aggiungere in un nuovo dizionario chiamato ordine, un primo, un secondo, un contorno, una bevanda ed un dolce preso dal menu'. 

ordine: dict = {"Pasta": 9.0, "Hamburger": 15.50, "Verdura del giorno": 7.00, "Coca Cola": 3.50,"Cheesecake": 6.00}

#  conto totale che il cliente dovrà pagare

conto_totale = (ordine["Pasta"]+ ordine["Hamburger"]+ ordine["Verdura del giorno"]+ ordine["Coca Cola"]+ ordine ["Cheesecake"])
print(f"Conto da pagare = {conto_totale}")

""" SPIEGAZIONE: Nella variabile conto_totale 
ho inserito il dizionario col nome: ordine e dopo con le ["nome della chiave]"""

# sotto c'e una seconda possibilità

conto_totale =sum(ordine.values())

# Stampa l'ordine totale

print(f"Conto da pagare = {conto_totale}")



   

