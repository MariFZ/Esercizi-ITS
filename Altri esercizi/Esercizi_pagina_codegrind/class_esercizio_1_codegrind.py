# Esercizi code - CLASSI

# Esercizio 1

# Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. 
# Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, ad esempio
#  “Ciao, mi chiamo Marco e ho 32 anni”.

# class Persona:

#     def __init__(self, nome:str, eta:int, sesso: str ):
#         self.nome = nome
#         self.eta = eta
#         self.sesso = sesso
    
#     def presentati(self):
#         print(f"Ciao, mi chiamo {self.nome}, ho {self.eta} e sono un {self.sesso}")
    
# marco:Persona = Persona("Marco", 32, "uomo")

# marco.presentati()

# Esercizio 2
# Creare una classe Animale che abbia gli attributi “nome” e “specie”. 
# Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. 
# Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.

# class Animale:
#     def __init__(self, nome:str, specie:str):
#         self.nome = nome
#         self.specie = specie
    
#     def emetti_suono(self):
#         if self.specie == "cane":
#             print(f"Il suono del {self.nome} e Bau!")
#         elif self.specie == "gatto":
#             print(f"Il suono del {self.nome} è Miau!")
#         else:
#             print(f"Non so quale suono fa l'animale: {self.nome}")

# animale1:Animale = Animale("Bender", "cane")
# animale2:Animale = Animale("Linda", "gatto")
# animale3:Animale = Animale("Gorro", "canarito")

# animale1.emetti_suono()
# animale2.emetti_suono()
# animale3.emetti_suono()

# Esercizio 3
# Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”. 
# Aggiungi un metodo “descrivi” che stampi una descrizione dell’automobile, 
# ad esempio “Questa è una Toyota Corolla del 2017”.

# class Automobile:

#     def __init__(self, marca:str, modello:str, anno:int):
#         self.marca = marca
#         self.modello = modello
#         self.anno = anno

#     def descrivi(self):
#         print(f"Questa è una {self.marca} {self.modello} del {self.anno}")

# macchina1:Automobile = Automobile("Toyota", "Corolla", 2017)

# macchina1.descrivi()

# Esercizio 4
# Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”. 
# Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% 
# e un metodo “stampa_dettagli” che stampi tutti i dettagli dell’impiegato, 
# ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.

# class Impiegato:

#     def __init__(self, nome:str, cognome: str, matricola:int, stipendio:float):

#         self.nome = nome
#         self.cognome = cognome
#         self.matricola = matricola
#         self.stipendio = stipendio

#     def aumenta_stipendio(self):
        
#         self.stipendio *= 1.1

#     def stampa_dettagli(self):
#         print(f"Impiegato: {self.nome} {self.cognome}, {self.matricola}, stipendio: {self.stipendio} ")

# impiegato1:Impiegato = Impiegato("Marco", "Rossi", 1234, 1000)
# impiegato1.stampa_dettagli()

# impiegato1.aumenta_stipendio()
# impiegato1.stampa_dettagli()

# Esercizio 5
# Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. 
# La classe dovrà avere i seguenti attributi:
# Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
# Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
# La classe dovrà avere i seguenti metodi:
# Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
# Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
# Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
# Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.

class GestoreMagazzino:

    # def __init__(self, prodotti:dict, costo_magazzino:list):
    #     self.prodotti = prodotti
    #     self.costo_magazzino = costo_magazzino

    def __init__(self,costo_magazzino:float):
        
        self.prodotti = {}
        self.costo_magazzino = costo_magazzino

    def aggiungi_prodotto(self, prodotto):
        
        self.prodotti[prodotto.nome] = prodotto
    
    def rimuovi_articolo(self, nome_prodotto):
        
        if nome_prodotto in self.prodotti:
            del self.prodotti[nome_prodotto]

    def calcola_costi_magazzino(self):

        costo_totale = 0
        for prodotto in self.prodotti.values():
            costo_totale += prodotto.scorta * self.costo_magazzino
        return costo_totale

class Prodotto:

    def __init__(self, nome:str, prezzo:float, scorta:int):
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta


# Crea alcuni oggetti prodotto
p1 = Prodotto("Telefono", 500, 10)
p2 = Prodotto("Tavolo", 1000, 5)

print(p1.nome, p1.prezzo, p1.scorta)

# Crea un oggetto GestoreMagazzino con un costo di magazzinaggio di 10 Euro per prodotto
gm = GestoreMagazzino(10)

# Aggiungi i prodotti al magazzino
gm.aggiungi_prodotto(p1)
gm.aggiungi_prodotto(p2)

# Calcola i costi di magazzino
print(gm.calcola_costi_magazzino())  # 150 (10*10 + 5*10)

gm.rimuovi_articolo("Telefono")

print(gm.calcola_costi_magazzino())  # 50 (5*10)



