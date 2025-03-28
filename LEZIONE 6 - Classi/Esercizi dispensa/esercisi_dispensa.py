# Esercisi dispensa

# Pag 18

# class MyClass:  # non aveva i due punti
#     def __init__(self, x): # self deve essere sempre scritto dopo il construttore: __init__
#         self.x = x

# obj:MyClass = MyClass() # qui devono essere scritte le parentesi
# print(object.x)

# pag 23

# class Animal:
#     def __init__(self, name:str, legs:str):
#         '''Una volta che si definiscono gli attributi, si devono chiamare sotto'''
#         self.name = name
#         self.legs = legs

# obj = Animal("Dog", 4)
# print(obj.name, obj.legs)

# pag 24
'''Esercizio 1'''

# 1. Copy the code and print the age of Bob (using the dot notation)
# 2. Create an if-statement that prints the name of the oldest of the two Persons
# 3. Create three other Persons. Make a list called people with all 5 Persons.
# 4. Make a loop that finds and prints the youngest person’s name


# class Person:

#     def __init__(self, name:str, age:int):

#         self.name = name
#         self.age = age

# alice:Person = Person("Alice W", 45)
# bob:Person = Person("Bob M", 36)


# # 1. print the age of Bob (using the dot notation)
# print(f"L'età del mio amico Bob è: {bob.age}")

# # 2. Create an if-statement that prints the name of the oldest of the two Persons
# # Prima possibilità

# # if alice.age > bob.age:
# #     print(f"La persona più adulta è: {alice.name}")
# # elif alice.age < bob.age:
# #     print(f"La persona più giovane è: {bob.name}")
# # else:
# #     print("Hanno la stessa età")

# # seconda possibilità usando la expressione ternaria: 
# ''' Modo compatto per scrivere un'istruzione if-else su una sola riga.
#     Con questa possibilità posso anche inserire i valori 
#     dentro una sola variabile e fare il confronto con gli attributi degli oggeti '''

# old_name = alice.name if alice.age > bob.age else bob.name


# print(f"{old_name} è il più veccchio")

# # 3. Create three other Persons. Make a list called people with all 5 Persons.

# giovanni:Person = Person("Giovanni", 23)
# paolo:Person = Person("Paolo", 80)
# francesca:Person = Person("Francesca", 60)

# person_list = [alice, bob, giovanni, paolo, francesca]

# # Col ciclo For posso inserire delle persone e il suo nomme 
# for i in range(5): # in questo caso faccio il range di 5 perchè voglio inserire 5 persone
#     person_list.append(Person(f"Persona_{i}", i + 40))
# #     # in questo caso al valore i do ipoteticamente l'età di 40

# # Posso inserire anche tramite input
# person_list = []  # Lista vuota all'inizio

# for i in range(5):  # Ripete il ciclo 5 volte per inserire 5 persone
#     nome = input(f"Inserisci il nome della persona {i + 1}: ")  # Chiede il nome
#     eta = int(input(f"Inserisci l'età di {nome}: "))  # Chiede l'età e converte in intero
#     person_list.append(Person(nome, eta))  # Aggiunge la persona alla lista

# # Stampa le persone inserite
# for person in person_list:
#     print(f"Nome: {person.name}, Età: {person.age}")


# print(len(person_list))
# # print(len(f"Queste sono le persone della mia lista: {person_list}"))

# # 4. Make a loop that finds and prints the youngest person’s name
# person = person_list[0]
# for p in person_list[1:]:
#     if p.age < person.age:
#         person = p

# print(f"Il più giovane è: {person.name}")



# Esercizio 2 pag 29 - dispensa

# 1. Scrivere una classe chiamata Studente con gli attributi nome (str) e programma di studio (str)
# 2. Creare tre istanze. Una per se stessi, una per il proprio vicino di sinistra e una per il nostro vicino di destra.
# 3. Aggiungere un metodo printInfo che stampi il nome e il programma di studio di uno studente. Testate il vostro metodo sugli oggetti!
# 4. Modificate il codice e aggiungete l'età e il sesso agli attributi. Modificare il metodo di stampa rispettivamente.

class Studente:
     
    def __init__(self, name:str, studio:str):
          self.name = name
          self.studio = studio
          self.age = 0
          self.gender = ""
    
    def printInfo(self):
        print(f"La persona: {self.name} è inscritta al corso di: {self.studio}")
    
    def setAge(self, age):
        self.age = age
        print(f"La persona si chiama {self.name}\n è inscritta al corso: {self.studio} e ha {self.age} anni")

    def setgender(self, gender):
        self.gender = gender
        print(f"La persona si chiama {self.name}\nè inscritt@ al corso: {self.studio} e ha {self.age} anni ed è {self.gender}")

    
    
mari:Studente = Studente("Mari", "Communicazione")
juan:Studente = Studente("Juan", "Ingenieria")
pauli:Studente = Studente("Pauli", "Diritto")


mari.printInfo()
juan.printInfo()
pauli.printInfo()

mari.setAge(23)
juan.setgender("uomo")



# mari:Studente = Studente("Mari", "Communicazione", 34, "donna")
# juan:Studente = Studente("Juan", "Ingenieria", 36, "uomo")
# pauli:Studente = Studente("Pauli", "Diritto", 30, "donna")

# Esercizio 3

# 1. Creare due istanze realistiche di Animali. 
# 2. Stampate il nome di ciascun oggetto
# 3. Modificare la quantità di zampe di un oggetto utilizzando la notazione dei punti.
# 4. Aggiungere un metodo setLegs() per impostare le gambe di un oggetto e ripetere il compito 3, ma questa volta utilizzando il metodo.
# 5. Aggiungere un metodo getLegs() per restituire la quantità di gambe.
# 6. Aggiungere un metodo chiamato printInfo che stampi tutti gli attributi dell'animale.

# class Animal:
     
#     def __init__(self, name:str, legs:int):
          
#           self.name = name
#           self.legs = legs
    
#     def setLegs(self, numero_zampe):
#          self.legs = numero_zampe

#     def getLegs(self):
#         return self.legs

#     def info(self):
         
#         print(f"Il nome del mio cane è: {self.name} e le sue zampe sono: {self.legs}")

# # creazione di due stanze

# cane:Animal = Animal("Bender", 4)
# papagallo:Animal = Animal("Gorro", 2)

# # Stampo il nome degli animali
# '''Utilizziamo l'attributo name per stampare il nome dell'animale'''
# print(cane.name)
# print(papagallo.name)

# # modifico il numero di zampe
# '''Modifico il numero di zampe con la notazione a punto'''

# cane.legs = 8

# print(cane.legs)


# #  4. Aggiungere un metodo setLegs() per impostare le gambe di un oggetto
# '''Il metodo è stato già definito sopra, quindi devo chiamarlo'''

# papagallo.setLegs(4) # di questa maniera aggiorno il numero di zampe! Questo papagallo ha 4! ;)

# print(papagallo.legs)


# #  5. Aggiungere un metodo getLegs() per restituire la quantità di gambe

# papagallo.getLegs()

# print(f"Questo papagallo è particolare, ha {papagallo.legs} zampe!")
         

# # 6. Aggiungere un metodo chiamato printInfo che stampi tutti gli attributi dell'animale

# papagallo.info()
# cane.info()

# Esercizio 4 (Folder 9 ex_4.py) - pag 34

# 1. Scrivere una nuova classe chiamata Cibo, che abbia come attributi nome, prezzo e descrizione come attributi.
# 2. Istanziate almeno tre cibi diversi che conoscete e che vi piacciono.
# 3. Creare una nuova classe chiamata Menu, che abbia un elenco (di cibi) come attributo.
# __init__ dovrebbe accettare un elenco di cibi come parametri opzionali (default=[]).
# 4. Creare un addFood() e un removeFood() per il menu.
# 5. Creare alcune nuove istanze di cibo. Aggiungere ciascuna di esse al menu utilizzando il rispettivo metodo.
# 6. Aggiungere un metodo printPrices() che elenchi tutte le voci del menu con i relativi prezzi.
# 7. Aggiungere un metodo di menu getAveragePrice() che restituisca il prezzo medio degli alimenti.

# from typing import Optional

# # 1. Scrivere una nuova classe chiamata Cibo, che abbia come attributi nome, prezzo e descrizione come attributi.
# class Cibo:

#     def __init__(self, nome:str, prezzo:int, descrizione:str):
#         self.nome = nome
#         self.prezzo = prezzo
#         self.descrizione = descrizione

# # 3. Creare una nuova classe chiamata Menu, che abbia un elenco (di cibi) come attributo.
# # Create a new class called Menu, it should have a list (of Foods) as attribute.
#     '''__init__ should take a list of Foods as optional parameters (default=[])'''
# class Menu:

#     # def __init__(self, foods: Optional[list] = None):
#     def __init__(self):
#     # def __init__(self, foods:list [Cibo] = None):

#         self.foods = []

       
# # 4. Creare un addFood() e un removeFood() per il menu
#     def addfood(self, food):

#         # if foods is None:
#         self.foods.append(food)
        
#         print(f"Questi sono i patti del Menu: {self.foods}")

# # 5. RemoveFood() per il menu
        
#     def removefood(self, food):
      
    


        # self.foods = [cibo for cibo in self.cibi if cibo.name != cibo.name]

    # def print_prices(self):
    #     for cibo in self.foods:
    #         print(f"{cibo.name}: €{cibo.prezzo:.2f}")

    # def get_average_price(self):
    #     if not self.cibi:
    #         return 0
    #     prezzo_totale = sum(cibo.prezzo for cibo in self.cibi)
    #     return prezzo_totale / len(self.cibi)


# # 2. Istanziate almeno tre cibi diversi che conoscete e che vi piacciono.
# cibo1:Cibo = Cibo("Hamburger", 15, "Fatto di carne, beacon e formaggio")
# cibo2:Cibo = Cibo("Patatine fritte", 8, "Piatto che si fa con patate e si mangia con el patate fritte")
# cibo3:Cibo = Cibo("Piadina", 8, "Piatto rotondo, dove puoi aggiungere tutto quello che vuoi")
# cibo4:Cibo = Cibo("Pasta alla carbonara", 17, "Piatto di pasta con pecorino e beacon.")
# cibo5:Cibo = Cibo("Risoto ai funghi", 9, "Riso fatto col brodo e funghi")



# menu:Menu = Menu()
# menu.addfood(cibo1.nome)
# menu.addfood(cibo2.nome)
# menu.addfood(cibo3.nome)
# menu.addfood(cibo4.nome)
# menu.addfood(cibo5.nome)
# print(menu)



# menu.print_prices()
# print(f"Prezzo medio: €{menu.get_average_price():.2f}")











        


        
     



