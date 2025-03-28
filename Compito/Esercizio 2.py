# Esercizio 2
# Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa. 
# Il risultato deve essere visualizzato in output.

# prima possibilita pensata da me:
frase:str = input("Scrive una frase per calcolare il numero totale di spazi presenti: ")
contatore_spazi:int = 0

for lettere in frase:
    if lettere == " ":
        contatore_spazi += 1

print(f"Il numero di spazio in frase: \"{frase}\" sono: {contatore_spazi}")

# seconda possibilità prendendo la lunghuezza della frase:
'''Risposta professore usando il metodo range'''

frase: str = input("Scrive la frase: ")

contatore_spazi:int = 0

for indice in range(len(frase)):
    if frase[indice] == " ":
        contatore_spazi += 1

print(f"Nella stringa\n\"{frase}\"\nci sono: {contatore_spazi}")

# analisi del ciclo con range


frase: str = input("Scrive la frase: ")

contatore_spazi:int = 0


# Scorre i caratteri della stringa, partendo dall'indice 4 fino all'indice 29 (perché range(4, 30)arriva fino a 29
for indice in range(4,30):

# Verifico che l'indice impostato sia minore della lunghezza della frase
    if indice < len(frase) and frase[indice] == " ":
        contatore_spazi += 1

print(f"Nella stringa\n\"{frase}\"\nci sono: {contatore_spazi}")














# # sbagliato: non ho letto bene la traccia

# parola: str= input("Inserisci una parola o una frase per calcolare il numero totale di spazi presenti: ")
# print(f"Il numero totale di spazi nella parola o frase che hai inserito: {parola} è: {len(parola)}")