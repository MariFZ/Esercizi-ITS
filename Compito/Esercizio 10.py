# Esercizio 10
# Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

# Il programma deve:

# acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
# calcolare e visualizzare la somma di tutti i numeri pari inseriti;
# calcolare e visualizzare la media di tutti i numeri dispari inseriti;
# determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
# se più numeri hanno la stessa frequenza massima, visualizzarli tutti.


# inizializzo le variabili

list_numeri:list[int] = []
somma_pari:int = 0
somma_dispari:int = 0
contatore_numeri_dispari = 0

while True:
    '''Chiedo all'utente di inserire un numero che deve essere diverso da zero'''

    primo_numero = int(input("Inserisci il primo numero intero: "))

    # si fa il controllo del numero 0 dall'inizio
    if primo_numero == 0:
        print("Il programma è terminato, hai inserito il numero 0")
        break
   
    if primo_numero%2 ==0: # controllo che il numero sia pare
        somma_pari += primo_numero # se è pare, l'aggiungo alla somma
        list_numeri.append(primo_numero) # aggiungo il numero alla lista
        
    elif primo_numero %2 != 0:  # se il numero è dispari
        somma_dispari += primo_numero # faccio la somma dei numeri dispai che mi serve per la media
        list_numeri.append(primo_numero) # aggiungo il numero alla lista dei numeri
        contatore_numeri_dispari += 1
        
    '''fino a qui ho fatto la verifica se il numero inserito:
        * se il numero è pari
        * se il numero è dispari
        * somma dei numeri pari
        * somma dei numeri dispari e anche contato quanti sono per fare la media
        # ho anche una lista dei numeri inseriti
    '''   

# creo un dizionario che me permetterà di capire quante volte un numero è ripetuto
'''
come funziona?
    * con un ciclo For controllo ogni numero presente nella lista dei numeri
    * verifico se il numero NON è presente nel dizionario
    * se non è presente, l'aggiungo al dizionario come:
        'chiave': numero - 'valore': 1  (il valore 1 mi dice che quel numero, si trova una volta)
    
        se invece il numero è già nel dizionario aggiungo il valore della chiave
        'chiave': numero - 'valore':  1 + 1 
'''
frequenze:dict = {}

for numero in list_numeri: # per ogni numero presente nella lista dei numeri
    if numero not in frequenze: # se il numero NON è presente
        frequenze[numero] = 1   # l'aggiungo al dizionario, con il valore 1
    else:
        frequenze[numero] += 1  # se invece è presente, aggiorno il valore della chiave + 1

'''Adesso devo verificare il numero più frequente
    Come si fa?
    
    Ho un dizionario: "frequenze" con tutti i numeri presenti nella lista,
    dove la chiave mi dice il numero di frequenze.

    1. Utilizzo la funzione: max() che prenderà il valore delle frequenze
        Questo si fa, così:
        Creo una variabile che prenderà questo valore
            - variabile = max(valore.values()) ---- Ricordare: .values() mi prende solo il valore della chiave
    
    2.  Creo una lista che prenderà il numero con le massime frequenze

    3.  Utilizzo il ciclo For per verificare che i numeri presenti nel dizionario,
        e vedere la loro frequenza.
        Per prendere sia la chiave e il valore, devo usare .items()

     '''

massima_freq = max(frequenze.values()) # creo la variabile che salverà la massima frequenza, nel valore
numeri_frequenti:list = []

for numero, frequenza in frequenze.items():
    '''for chiave, valore in dizionario.items()'''
    if frequenza == massima_freq:
        '''se la frequenza che ai trovato è uguale alla massima frequeza, 
            aggiungela alla lista: "numeri_frequenti'''
        numeri_frequenti.append(numero)

        

print(f"La lista dei numeri è {list_numeri}, la somma dei numeri pari è: {somma_pari}, la somma dei numeri dispari: {somma_dispari} la media dei numeri dispari è: {(somma_dispari/media)} e la massima frequenza di numeri: {numeri_frequenti} {massima_freq} volte")


# soluzione senza la frequenza fatta abbastamza bene, ma non ho creato un dizionario


# list_numeri:list[int] = []
# somma_max_frequenza:list[int] = []
# somma_pari:int = 0
# somma_dispari:int = 0
# media = 0

# primo_numero = int(input("Inserisci il primo numero intero: "))

# if primo_numero !=0:
#     # max_frequenza = primo_numero

#     if primo_numero%2 ==0:
#         somma_pari += primo_numero
#         list_numeri.append(primo_numero)
        
#     elif primo_numero %2 != 0:
#         somma_dispari += primo_numero
#         list_numeri.append(primo_numero)
#         media +=1

# else:
#     print("Hai inserito il numero zero")

# while True:
#     secondo_numero = int(input("Inserisci il primo numero intero: "))
    
    
#     if secondo_numero > 0:
#         if secondo_numero%2 ==0:
#             somma_pari += secondo_numero
#             list_numeri.append(secondo_numero)
   
#         elif secondo_numero % 2 != 0:
#             somma_dispari += secondo_numero
#             list_numeri.append(secondo_numero)
#             media +=1

#         if secondo_numero == max_frequenza:
#             somma_max_frequenza.append(secondo_numero)
#     else:
#         break          
# print(f"La lista dei numeri è {list_numeri}, la somma dei numeri pari è: {somma_pari}, la somma dei numeri dispari: {somma_dispari} la media dei numeri dispari è: {somma_dispari/media} e la massima frequenza di numeri: {somma_max_frequenza}")

        


