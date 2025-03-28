# Esempio dispensa: Functions

# pag 17

# Esistono alcune funzioni che eseguono determinate istruzioni senza restituire alcun valore.
# In questo caso, l'istruzione return viene omessa per indicare che la funzione non restituisce alcun valore.

# -------
# ESEMPIO

# def greet(name:str) -> None:

#     print(f"Hello {name}")

# greet("Mari")

# --------------------- 
# pag 18


# In Python, una funzione può restituire più di un valore utilizzando tuple, liste o dizionari. 
# Il metodo più comune è la restituzione di una tupla, in cui i valori sono separati da una virgola dopo l'istruzione return.

# ESEMPIO
# -------

# def operations(a: int, b: int) -> tuple[int, int]:

#     somma: int = a + b
#     sotrazione: int = a - b
    
#     return somma, sotrazione


# numeroa: int = 34
# numerob: int = 35

# Il valore delle due operazioni può entrare nel print, oppure 

# print(f"Risultato con due valori dentro 2 variabili.  La funzione ha dentro la variabili: {operations(numeroa,numerob)}")

# Oppure si possono creare 2 variabili come si spiega sotto:

# ATTENZIONE:   Per farlo vedo scrivere prima il nome delle variabili separate da virgola:
#               "somma_numeri","sotrazione_numeri" e dopo chiamo la funzione, tra parentesi scrivo i valori 
#               o come nell'esempio scrivo la variabile alle quale sono state assegnate.

# somma_numeri, sotrazione_numeri = operations(58, 69)

# print(f"Questa è la somma: {somma_numeri}")
# print(f"Questa è la sotrazione: {sotrazione_numeri}")


# print(f"Questo è il risultato della seconda somma e sotrazione, SENZA creare variabili: {operations(58,69)}")

# # pag 19
# # definire una funzione che restituisce un elenco

# def get_coordinate(x: int, y: int) -> list[float]:

#     return [x,y]

# coord: float = get_coordinate(12.45, 12.5)

# print(f"Questo è il valore: {coord[0], coord[-1]}")

# print(type(coord))

# pag 21

# Funzioni con parametri passati per posizione

# Gli argomenti dell'istruzione vengono abbinati ai parametri dell'intestazione della funzione in base al loro ordine.
# Ovvero,
#    ● Il primo argomento viene passato al primo parametro,
#    ● Il secondo argomento viene passato al secondo parametro e così via.

# def describe_person(name: str, age: int, city: str):

#     print(f" Questo è il mio nome: {name}, la mia età è: {age} e la mia città: {city}")

# describe_person("Mari", 23, "Roma")

# print(describe_person)


# pag 22 Secondo esempio per parametri chiamati PER POSIZIONE

# def greet(name: str, age: int) -> None:
#     print(f" Hello! My name is {name} and I'm {age} years old!")

# greet("Angela", 23) # chiamata per posizione

# # QUESTO NON SAREBBE CORRETTO PERCHE STAMPA UN'ALTRA COSA IN UNA POSIZIONE DIVERSA
# greet(34, "Mari")

# # pag 23    Funzioni con parametri passati per parola chiave/1

# def describe_person(name:str, age:int, city:str):               # Definisco la funzione
    
#     print(f"{name} is {age} years old and lives in {city}.")    # Imposto come voglio il print


# describe_person(age=25, city= "Rome", name="Alice") # chiamata per keyword

# describe_person(city= "Rome", age=25, name= "Alice")


# pag 24  Gli argomenti passati per posizione deveono precedere quelli passati per parola chiave

#  # nome: ALice è riconosciuto per posizione, gli altri per parola chiave

# pag 26 ------ Funzioni con valori PREDEFINITI/1 ----

# Alcuni (o tutti) i parametri di una funzione possono avere valori predefiniti, 
# ovvero valori che vengono assegnati loro quando non vengono passati valori come argomenti di input.

def total(w, x, y=10, z=20):
    return (w ** x) + y + z 

# calcula  2^3 + 10 + 20. = 38 In questo caso, ho omesso gli ultimi due valori
 
print(total(2,3))

# stesso esercizio ma omettendo solo l'ultimo valore

print(total(2,3,4))   # calcula 2^3 + 4 + 20 = 32

# stesso esercizio con tutti valori diversi, cioè cambiando quelli di default

print(total(2,3,4,5)) # risultato = 17

# pag 27 ---- Funzioni senza parametri


# Alcune funzioni possono essere definite ed eseguite senza ricevere alcun valore di ingresso o parametro.
# In Python, le funzioni non sempre richiedono argomenti per eseguire un'azione. 
# Le funzioni SENZA PARAMETRO, sono utili quando un compito deve essere eseguito in modo standard,
# senza dipendere da input esterni.

def hello():
    print("Hello")

hello()  # in questo caso non abbiamo inserito la funzione dentro una variabile

def get_pi():
    # print(float(3.14159))
    return 3.14159

pi_value:float= get_pi()   # ho chiamato la funzione dentro una variabile
# Se una funzione deve restituire un valore, 
# significa che il suo output sarà utilizzato in altre parti del programma, 
# ad esempio per assegnare una variabile o per passare il risultato a un'altra funzione.

print(f"The value of pi is: {pi_value}")


# DA RICORDARE:

# Se il RISULTATO della funzione deve essere utilizzato in altre parti del programma,
# è utile restituire un valore.

# Se la funzione deve lavorare con dati esterni forniti dall'utente o dal programma, 
# è utile accettare parametri.

# Se la funzione esegue solo un'azione (come la stampa di un messaggio), 
# potrebbe non avere bisogno né di parametri né di valori di ritorno.

# pag 30

# FUNZIONI CALLS AND EXECUTION

def max(num1: int, num2: int) -> int:

    if num1 > num2:
        return num1
    else:
        return num2

# chiamo la funzione nel print

print(f" Il numero maximo è: {max(3,4)}")

# creo invece una variabile che contiene i due valori

num_max: int = max(3,4)
print(f" Il numero massimo dentro la variabile \"num_max\" è: {num_max}")

# l'inserisco invece in una variabile

# primo_numero: int = int(input("Scrive il primo numero: "))
# secondo_numero: int = int(input("Scrive il secondo numero: "))

# num_max2: int = max(primo_numero, secondo_numero)

# print(f" Il numero massimo dentro la variabile \"num_max\" è: {num_max2}")

# pag 34 -- Funzione args

# Consente di passare un numero illimitato di valori ad una funzione

def add(*args): # Accepts multiple numbers in input
    total = 0

    for number in args:
        total += number
    return total

print(add(2, 3)) # Output 5
print(add(10, 20, 30)) # Output 60

# pag 37 -- Funzione kwargs

# per passare coppie chiave-valore (nome e prezzo)

def total_price(**kwargs):
    total:float= 0
    
    for product, price in kwargs.items():
        print(f"{product}: {price}€")
        total += price
        return round(total, 2)
    
print(total_price(coffee=2.99, cake=4.55, juice=2.99))

