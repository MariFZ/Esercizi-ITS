# ESERCIZI

A =  "1.1 DIMOSTRAZIONE DEL VALORE APROSSIMATIVO DEI NUMERI FLOAT"
x: float = 10.80
y: float = 1.0/10.80

print(A)
print(f" Valore della variabile Y dopo questa operazione: y: float = 1.0/10.80 è=  {y}") 
print(f" Valore della variabile X è=  {x}") 

prodotto = (x*y)
print(f"Questo è il risultato del prodotto tra X e Y: {prodotto} + che dovrebbe essere 0.9999999")

print(x  -(x*y))


# ESERCIZIO 1.2 

B ="1.2 ESERCIZIO CON L'USO DELL'OPERATORE MODULO (%) E LA VARIABILE X POSITIVA E NEGATIVA"
x: float = 35.50
y: float = x % 2.50 # l'operatore % (modulo) calcola il resto della divisione intera tra due numeri.

print(B)
print(f"Questo è il risultato del resto dell'operazione x % 2.50 , quindi y è = {y}")
print(x)

# valori + negativi nella variabile x

x: float = - 35.50
y: float = x % 2.50 # l'operatore % (modulo) calcola il resto della divisione intera tra due numeri.
print(f"Questo è il risultato del resto dell'operazione dove x è negativa: x % 2.50 , quindi y è = {y}")
print(x)

# 1-3

C= "1.3 Scriva un programma che legge tre numeri interi e visualizza la media dei tre numeri"
C_1 = "Soluzione N°1"
print(C)
print(C_1)

numeri: list = [10, 200, 24]
somma = sum(numeri)
print(f"La somma dei tre numeri è questa: {somma}")

media = somma / 3 
print(f"La media dei tre numeri è questa con la soluzione N°1: {media}")

C_2 = "# Soluzione N°2"
print(C_2)

numeri: list = [10, 200, 24]
media = sum(numeri) / len(numeri)
print(f"La media dei tre numeri è questa con la soluzione N°2 = {media}")

# ESERCIZIO 1.4
D = "1.4 Scriva un programma che dato un intero di quattro cifre, per esempio 2024, lo si visualizzi, una cifra per riga"
print(D)

numero_intero: int= 3333
for cifra in str(numero_intero): 
    print(cifra)

# ESERCIZIO 1.5
E = "1.5 Si scriva un programma che converta la temperatura da Fahrenheit a Celsius "
print(E)

gradi_fahrenheit = int(input("Inserisci la temperatura che desideri cambiare ")) # si deve dare un numero intero
conversione = 5*(gradi_fahrenheit-32)/9  # Il risultato sarà in float, anche se l'input è un intero, perchè le divisioni sono sempre in decimale
print(f"{gradi_fahrenheit} ° gradi Fahrenheit corrispondono a {conversione:.1f} gradi Celsius")

# ESERCIZIO 1.6
F = "1.6 Creare un dizionario col nome Menu. Aggiungere in un nuovo dizionario chiamato ordine, un primo, un secondo, un contorno, una bevanda ed un dolce preso dal menu'. Quanto è il conto?"
print(F)

menu: dict = {"Pizza": 9.0, "Pasta": 10.50, "Zuppa": 7.0, "Hamburger": 15.50, "Cotoletta": 10.00, "Salmone": 20.20, "Patatine fritte": 5.50,"Patate al forno": 5.50, "Verdura del giorno": 7.00, "Cheesecake": 6.00, "Tiramisu": 6.00, "Focaccia con Nutella": 6.00, "Coca Cola": 3.50, "Acqua": 1.50, "Vino": 5.0}

ordine: dict = {"Primo": "Pasta", "Secondo": "Hamburger", "Contorno":"Verdura del giorno", "Bevanda": "Coca Cola", "Dolce": "Cheesecake"}

F_1 = "PRIMA SOLUZIONE CREANDO UNA VARIABLE VUOTA = TOTALE"
print(F_1)

totale = 0.0
for piatti in ordine.values():
    totale += menu[piatti]

print(f"Totale: {totale}")

F_2 = "SECONDA SOLUZIONE USANDO LA FUZNIONE SUM"
print(F_2)

conto = sum(menu[item] for item in ordine.values())
print(f"Il totale del conto è: {conto}€")


F_3 = "SOLUZIONE SE VOLESSE AVERE IL VALORE DI TUTTO IL MENU"
print(F_3)

conto_totale =sum(menu.values())
print(f"Conto da pagare = {conto_totale}")


# 2.3 Messaggio personale

nome: str = "Jean Paul"
print("Ciao " + nome + ", ti piacerebbe imparare un po' di Python oggi?")

# 2.4 Casi di nomi

nome: str ="Tatiana"
print("Ecco il tuo nome " + nome  + " in maiuscola: " + nome.upper() + " . Adesso tutto in minuscolo: " + nome.lower() + "\ne per ultimo, tutto in titolo: " + nome.title())

# 2.5 e 2.6 Frase di una persona famosa

autore: str = "Albert Einstein"
frase: str = "La mente è come un paracadute. Funziona solo se si apre" 
print(autore + " una volta disse: '" + frase +"'." )

# 3.1: Prima soluzione

nomi: list = ["Anna Maria", "Javier", "Manuela", "Andrew", "Francesco"]
for amici in nomi:
    print(amici)

print("\n".join(nomi) + "\n" + "con questa possibilità con join: variabile.join si riesce a mettere tutti i nomi in fila" )

# 3.2

nomi: list= ["Anna Maria", "Javier", "Manuela", "Andrew", "Francesco"]
messaggio: str = "Buone Feste:"

for amici in nomi:
        print(messaggio, amici)


# 3.3

trasport: dict = {"bicicleta": 1, "macchina": 2,  "aereo": 3}
text: dict = {"Mi piace andare in bici perché mi regala paesaggi stupendi ad ogni pedalata.": "bicicleta","Mi piace guidare e ascoltare musica, perché trasforma ogni viaggio in un momento di libertà e relax.": "macchina","Salire su un aereo è come aprire una porta magica: in un attimo sei tra abbracci di parenti lontani o avventure in posti incredibili!": "aereo"}

for frase, mezzo in text.items(): # dichiarazione di 2 variabili
   print(f"{frase} - Mezzo di trasporto preferito: {trasport[mezzo]}")


# 3.4

invitati: list = ["Andrew", "Manuele", "Chiara"]
# messaggio: str = "Ti invito a cena per condividere buon cibo, risate e momenti piacevoli insieme!"

for invito in invitati: 
    print(f"{invito}: " + "Ti invito a cena per condividere buon cibo, risate e momenti piacevoli insieme!")

# 3.5 

invitati_1: list = ["Andrew", "Manuele", "Chiara"]
invitati_2: list = ["Andrew", "Manuele", "Jean Paul"]

for invito in invitati_2: 
    print(f"{invito}: " + "Ti invito a cena per condividere buon cibo, risate e momenti piacevoli insieme!")

assenza = invitati_1[2]

print(f"Purtroppo, " + assenza + " non potrà venire a questa festa")

# 3.6

invitati_1: list = ["Andrew", "Manuele", "Chiara"]
invitati_2: list = ["Elena", "Sofia", "Isabella"]
messaggio: str = "Giacché abbiamo trovato una tavola più grande, ci sarà cibo per tutti… e qualche porzione in più!"

invitati_1.insert(0, "Elena") # Il metodo insert() richiede due argomenti: l'indice e l'elemento stesso
print(invitati_1)

invitati_1.insert(2, "Sofia") 
print(invitati_1)

invitati_1.append("Isabella") # L'inserisce alla fine
print(invitati_1)

for invito in invitati_1: 
    print(f"{invito}:   Ti invito a cena per condividere buon cibo, risate e momenti piacevoli insieme! \n{messaggio}" )

# 3.7

invitati_1: list = ['Elena', 'Andrew', 'Sofia', 'Manuele', 'Chiara', 'Isabella']
messaggio: str = "Abbiamo trovato una tavola più grande, peccato che non arriverà mai, quindi possiamo ospitare solo 2 persone!"

for invito in invitati_1:
    print(f"Ciao {invito},  abbiamo una triste notizia...  \n{messaggio}")


# 3.6

F = "ESERCIZIO 3.6"
print(F)

invitati_1: list = ['Elena', 'Andrew', 'Sofia', 'Manuele', 'Chiara', 'Isabella']
print(invitati_1)

messaggio: str = "Abbiamo trovato una tavola più grande, peccato che non arriverà mai, quindi possiamo ospitare solo 2 persone!"
messaggio_personale: str = "Non possiamo averti più tra noi, ma ti manderemmo un pezzo di torta"
for invito in invitati_1:
   print(f"Ciao {invito},  abbiamo una triste notizia...  \n{messaggio}")
 
invitati_1.pop(0) 
print(f"Ciao {invitati_1[0]} e   abbiamo una triste notizia... \n{messaggio_personale}")

invitati_1.pop(0) 
print(f"Ciao {invitati_1[0]},  abbiamo una triste notizia... \n{messaggio_personale}")

invitati_1.pop(0) 
print(f"Ciao {invitati_1[0]},  abbiamo una triste notizia... \n{messaggio_personale}")

len(invitati_1)
print(invitati_1)

invitati_1.pop(0) 
print(f"Ciao {invitati_1[0]},  abbiamo una triste notizia... \n{messaggio_personale}")

len(invitati_1)
print(invitati_1)

# invito alle 2 persone rimaste
print(f"Ciao {invitati_1[0]} e {invitati_1[1]}  siamo felici di accogliervi a casa nostra")

del invitati_1 [:]
print(invitati_1)

# ESERCIZIO 3.8
G = "ESERCIZIO 3.8"
print(G)

città: list = ["New York", "Canada", "Mexico", "Cina", "Peru"]
# print(f"Questo è l'elenco delle città che mi piacerebbe visitare un giorno: {città}") # così stampa con le []


print(f"Questo è l'elenco delle città che mi piacerebbe visitare un giorno: {', '.join(città)}")

print(f"Questo è l'elenco delle città che mi piacerebbe visitare un giorno in ordine alfabetico: {', '.join(sorted(città))}")

print(f"Lista ancora nel suo ordine originale: {' , '.join(città)}")

città.reverse()
print(f"Questo è l'elenco delle città che mi piacerebbe visitare un giorno in ordine alfabetico alla rovescia: {', '.join(città)}")

print(f"Lista modificata nel suo ordine originale dopo l'uso di reverse: {' , '.join(città)}")

città.reverse()
print(f"Questo è l'elenco delle città che mi piacerebbe visitare un giorno ordinato nuovamente all'ordine originale: {', '.join(città)}")

città.sort()
print(f"Questo è l'elenco delle città che mi piacerebbe visitare un giorno memorizzato in ordine alfabetico: {', '.join(città)}")


città.sort()
print(f"Questo è l'elenco delle città che mi piacerebbe visitare un giorno memorizzato in ordine alfabetico inverso: NON MI FUNZIONA {', '.join(città)}")

H = "ESERCIZIO 3.9"
print(H)

invitati_1: list = ['Elena', 'Andrew', 'Sofia', 'Manuele', 'Chiara', 'Isabella']
print(f"Questo è il numero di persone invitate a cena: {len(invitati_1)}") # LEN: DA IL NUMERO DI ELEMENTI NELLA LISTA

# 6.1

I = "ESERCIZIO 6.1"
print(I)

persona_1: dict = {"Nome": "Natalia", "Cognome": "Brand", "Età": "35", "Città": "Roma"}
messaggio: str = "Questa è l'informazione della mia amica"

print(messaggio)

for amica in persona_1.items():
    print(': '.join(amica))

J = "ESERCIZIO 6.1 DOVE IL VALORE DI ETA E' UN INTERO"
print(J)

persona_1: dict = {"Nome": "Natalia", "Cognome": "Brand", "Età": 35, "Città": "Roma"}
messaggio: str = "Questa è l'informazione della mia amica"

for amica in persona_1.items():
    print(': '.join(str(item) for item in amica))


# 6.2 

J = "Esercizio 6.2 = Numeri preferiti"
print(J)

name_number: dict = {"Natalia": 10, "Andrew": 6, "Chiara": 14, "Jean Paul": 2, "Manuel": 24}
for name, number in name_number.items(): # FUNZIONE .items ()
    print(f"{name}: {number}")


# 6.3 

K = "Esercizio 6.3 = Glossario"
print(K)

glossario: dict = {"Items": "Funzione che itera tra le chiavi e il valore, dando i due dati separati ", "Insert": "Richiede 2 argomenti: l'indice dove inserire l'elemento e il nome dell'elemento stesso", "Join": "Usata solo per iterare sulle stringe. Nella sintassi, si deve specificare come separare gli elementi (si devono mettere tra virgolette come si vogliono separare, seguito di .join" , "Funzione Len": "Si scrive prima della variabile per vedere gli elementi", "Metodo Pop": "Rimuove un elemento con questa sintassi: variabile.pop()"}
for parola, significato in glossario.items():
    print(f"\n{parola}: \n{significato}")

# 6.7


persona_1: dict = {"Nome": "Natalia", "Cognome": "Brand", "Età": 35, "Città": "Roma"}
persona_2: dict = {"Nome": "Tatiana", "Cognome": "Brand", "Età": 30, "Città": "Spagna"}
persona_3: dict = {"Nome": "Paulina", "Cognome": "Brand", "Età": 25, "Città": "Roma"}

list_persone: list = [persona_1, persona_2, persona_3]


for persona in list_persone:
    print(f"Nome: {persona['Nome']}, Cognome: {persona['Cognome']}, Età: {persona['Età']}, Città: {persona['Città']}")


# 6.8 

# Animali domestici

animale_1: dict= {"tipo di animale": "cane", "nome": "Bender", "razza": "Westie", "età": "12", "nome proprietario": "Andrew"}
animale_2: dict= {"tipo di animale": "gatto", "nome": "Stella", "razza": "Maine Coon", "età": "12", "nome proprietario": "Mauro"}
animale_3: dict= {"tipo di animale": "pappagallo", "nome": "Gorro Frio", "razza": "Cocorito", "età": "5", "nome proprietario": "Paulina"}
animale_4: dict= {"tipo di animale": "pesce rosso", "nome": "Fish", "razza": "Cometa", "età": "10", "nome proprietario": "Francesco"}


animali_domestici: list= [animale_1, animale_2, animale_3, animale_4]

for animale in animali_domestici:
    print(f"tipo di animale: {animale['tipo di animale']}, Nome: {animale['nome']}, Razza: {animale['razza']}, Eta: {animale['età']}, Nome Proprietario: {animale['nome proprietario']}")



# 6.9 LUOGHI PREFERITI

luoghi_favoriti: dict = {"Noemi": "Paraguay", "Gustavo": "Brasile", "Sara": "Italia"}


print("Questo è l'elenco dei nostri amici. Vuoi scoprire il paese favorito di: ", ", ".join(luoghi_favoriti.keys()))

nome = input("Inserisci un nome per conoscere il suo luogo preferito: ")

if nome in luoghi_favoriti:
    print(f"Per {nome}, il luogo favorito è {luoghi_favoriti[nome]}.")
else:
    print(f"Il nome {nome} non è presente nella lista dei luoghi preferiti.")


"Esercizio 6.10 = Più numeri preferiti per persona"

first_number: dict = {"Natalia": 10, "Andrew": 6, "Chiara": 14, "Jean Paul": 2, "Manuel": 24}
second_number: dict = {"Natalia": 7, "Andrew": 8, "Chiara": 1, "Jean Paul": 23, "Manuel": 33}

for persona in first_number:
    # Recupera il numero preferito dalla persona in entrambi i dizionari
    primo_numero = first_number[persona]
    secondo_numero = second_number[persona]
    
    print(f"{persona}: {primo_numero}, {secondo_numero}")


# 6.12

città: dict = {"Manila": "Filippine" , "Firenze": "Italia", "Barcellona": "Spagna"}

città_manila: dict = {"Paese": "Filippine", "Popolazione": "1.846.513", "Fatto": "La città ospita uno dei più antichi e più grandi cimiteri per animali del mondo: il Cimitero degli Animali di Manila"}

città_firenze: dict = {"Paese": "Italia", "Popolazione": "362,643", "Fatto": "A Firenze, nel 1587 è nato il gelato moderno!"}

città_barcellona: dict = {"Paese": "Spagna", "Popolazione": "1.656.725", "Fatto": "La città è famosa per avere uno dei più grandi sistemi di biciclette pubbliche del mondo"}

print("Questo è l'elenco di 3 città che conosco. Vuoi scoprire i dati di: ", ", ".join(città.keys()))

nome = input("Inserisci un nome di una città presente nell'elenco: ")

if nome in città:
    if nome == "Manila":
        informazione = città_manila
    elif nome == "Firenze":
        informazione = città_firenze
    elif nome == "Barcellona":
        informazione = città_barcellona
   
    print(f"Città: \n{nome}, \nPaese: {informazione['Paese']}, Popolazione: {informazione['Popolazione']}, \nFatto: {informazione['Fatto']}")
    
else: 
        print("Mi dispiace, mi sembra che non conosco ancora quella città")



