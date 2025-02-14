# prova di creazione di dictionario e l'aggiunta di nuovi elementi

menu_estivo: dict = {"Pizza": 15, "Pasta": 10, "Insalata": 5}
menu_invernale: dict = {"Pizza": 20, "Pasta": 15, "Insalata": 10}

menu_estivo["dessert"] = 30
print(menu_estivo)

menu: dict = {}
menu["menu_estivo"] = menu_estivo
menu["menu_invernale"] = menu_invernale
print(menu)


menu["menu_estivo"].pop("Pizza")
print(f" Questo è il numeo menu senza la Pizza del Menu estivo perchè Manu non vuole = {menu=}")

menu["menu_invernale"].pop("Pizza")
print(f" Questo è il menu senza la Pizza del Menu invernale perchè troppo lavoro = {menu=}")

# prezzo = menu["menu_estivo"].pop("Pizza") # POP rimuove un elemento dal dizionario: Pizza del menu estivo
# print(prezzo)

# print(f"{prezzo}") # mi fa vedere il prezzo di pizza che è stato cancellato


# print(f"{menu=}")

# 






'''

'''

# COME MODIFICARE IL VALORE DI UNA CHIAVE DENTRO UN DIZIONARIO!!!
''' si scrive il dictionary e dopo '''

""""
menu["menu_estivo"]["Pizza"] = 150 # così modifico il valore della pizza del menu estivo
print(menu_estivo)

menu["menu_invernale"]["Pasta"] = 45
print(menu_invernale)"""








