# dichiarazione di un dizionario

m: dict = {"a": 1, "b": 2, "c": 3}
# aggiunta di un elemento al dizionario: si scrive il nome della variabile, se mette [""]  
m["d"] = 4
print(m)

variabile: int =m["a"] # sto inserendo alla variabile il valore "a" del dictionary che sarebbe 1
print(variabile)
print(f"{variabile=}") # f per formattare la stringa
print(f"Il valore di {variabile=}")  

c: dict = {"i": 1, "j": 2, "k": 3}
m["inner"] = c # chiave con nome di inner che sarebbe così come risultato: 'inner': {'i': 1, 'j': 2, 'k': 3}
print(m) 

m["inner"]["k"] # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'inner': {'i': 1, 'j': 2, 'k': 3}}
print(m)

lista_1: list = [1,2,3,4, [2,3,4]]
print(lista_1[4][1]) # da come valore 3

menu: dict = {"menu_estivo":{"Pizza": 15, "Pasta": 10, "Insalata": 5}}
menu["menu_estivo"]["Pasta"]
print(menu)

menu_invernale: dict = {"Pizza": 20, "Pasta": 15, "Insalata": 10}
menu["menu_invernale"] = menu_invernale
print(menu)

menu["menu_estivo"]["Bistecca"] = 25
print(menu)    
menu["menu_invernale"]["Bistecca"] = 30
print(menu)
menu[]