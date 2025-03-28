# ESERCIZIO 9

# Classifica delle vendite

# Progetta un algoritmo che forniti dall'utente 20 totali di vendita e i nomi dei venditori,
# trova i due nomi dei venditori con il totale più alto e il totale più basso delle vendite.

# nome_vendita = dict(input({"Andrea": 30, "Giovanni": 45, "Mary": 43, "Tatiana": 39, "Paulina": 37, "Diego": 40, "Pedro": 73, "Fanny": 72}))

max_nome = str("")
max_vendita = float('inf')
min_nome = str("")
min_vendite = float('inf')
cont = 0

while cont < 3:
    new_nome = str(input("Inserisci il nome del venditore:"))
    new_vendite = int(input("Inserisci il valore della vendita: "))
                            
    if new_vendite > max_vendita:
        max_nome = new_nome
        max_vendita = new_vendite
    if new_vendite < min_vendite:
        min_nome = new_nome
        min_vendite = new_vendite
    cont += 1


print(f"Il venditore con maggiore vendite è: {max_nome} e il massimo delle sue vendita è: {max_vendita}")
print(f"Il venditore con minore vendite è: {min_nome} e il minimo delle sue vendite è: {min_vendite}")






