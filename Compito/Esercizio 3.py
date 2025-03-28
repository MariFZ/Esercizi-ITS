# Esercizio 3
# Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale. 
# Il programma deve poi visualizzare la stringa ottenuta in output. 
# Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.

# Soluzione usando il ciclo while
# parola:str = input("Inserisci la parola che desideri invertire: ")

# parola_invertita:str = ""
# conta_lettere:int = 0

# while conta_lettere < len(parola):

#     # creo una variabile volatile col nome lettera (sarà di tipo intero così mi prende i numeri) e prendo l'ultima parola
#     lettera = parola[-(conta_lettere +1)]   # somma degli indici alla rovescia sino stampa sempre l'ultima parola. 
#     '''Ricordare: 
#         giacchè devo andare alla rovescia, posso fare la somma del contatore, 
#         ma basta mettere il segno - prima delle parentesi'''

#     parola_invertita += lettera
#     i += 1
# else:
#     print(f"La parola invertita è: {parola_invertita}")


# Soluzione col ciclo For

# parola: str = input("Scrive la parola: ")

# parola_invertita:str = ""
# cont_lettere:int = 0

# for lettera in parola:

#     lettere = parola[-(cont_lettere + 1)]
#     parola_invertita += lettere
#     cont_lettere += 1

# print(parola_invertita)

# Soluzione MOLTO PIU SEMPLICE
'''risposta professore'''

parola:str = input("Scrive una parola: ")

parola_invertita:str = ""

for lettera in parola:
    parola_invertita = lettera + parola_invertita
    ''' Cosa sto facendo qui?

        Usando il ciclo for, sommo le lettere alla rovescio:

        Per esempio ho la parola = amor
        alla prima iterazione prendo la lettera: "a", alla seconda: "m" e cosi via:

        Attenzione: La chiave sta nella posizione della somma
        Vediamolo!

        parola invertita = parola + parola invertita
            * Prima iterazione: a + parola invertita(vuoto)
            * Seconda iterazione: m + parola invertita(a)
            * Terza iterazione: o + parola invertita (ma)
            * Quinta iterazione: r + parola invertita (oma)

        Non ci sono più lettere in parola, quindi parola invertita sarà:

        parola invertita = roma

        Se invece voglio copiare le parole nello stesso ordine, 
        bastava cambiare l'ordine della somma:

        parola invertita: parola invertita + parola
        
        '''

print(parola_invertita)






# SOLUZIONE CONSEGNATTA: QUASI CORRETTA MA L'HO FATTA CON UNA LISTA E NON UNA STRINGA

# Chiedo all'utente di scrivere una parola
# parola: str = input("Scrive una parola: ")

# # creo una variabile vuota che prenderà le lettere alla rovescio di parola
# stringa_invertita: str = ""

# contatore_rovescia = 0

# while contatore_rovescia <= len(parola):
#     stringa_invertita = parola[-(contatore_rovescia + 1)]
#     contatore_rovescia +=1

# print(f"La prola invertita è: {stringa_invertita}")



