# Ripaso

# Da compito - Esercizio 10
# Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

# Il programma deve:

# acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
# calcolare e visualizzare la somma di tutti i numeri pari inseriti;
# calcolare e visualizzare la media di tutti i numeri dispari inseriti;
# determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista
# se più numeri hanno la stessa frequenza massima, visualizzarli tutti.

# somma_pari = 0
# somma_dispari = 0
# lista_dispari:list = []
# somma_dispari = 0


# lista_numeri:list[int] = []

# while True:
#     '''finchè non si scrive il numero 0'''
#     numero = int(input("Inserisce un numero intero, cioè senza virgola: "))
#     if numero == 0:
#         print(f"Hai inserito: {numero}!")
#         break
    
#     elif numero % 2 == 0: # se % 2 da 0, cioè si è pari
#         somma_pari += numero # aggiungo alla somma dei numeri pari
#         lista_numeri.append(numero) # aggiungo il numero alla lista totale
  
#     else:
#         somma_dispari += numero # se invece no, l'aggiungo alla somma dei dispari
#         lista_dispari.append(numero) # aggiungo il numero alla lista totale
        

# frequenze:dict = {}

# for number in lista_numeri:
#     if number not in frequenze:
#         frequenze[number] = 1
#     else:
#         frequenze[number] += 1


# max_frequenza = max(frequenze.values()) # questa varaibile memorizza il valore massimo del dizionario
# piu_frequenti:list = []

# for number, frequenze in frequenze.items():
#     if frequenze == max_frequenza:
#         piu_frequenti.append(number)




# print(f"Questa è la somma dei numeri pari: {somma_pari}, la media dei dispari: {somma_dispari/len(lista_dispari):.2f} e il numero più frequente: {piu_frequenti}{max_frequenza} volte")

def solveMeFirst(a,b):
	# Hint: Type return a+b below

    somma = a + b
    
    return somma
    

num1 = int(input("Inserisce un numero1: "))
num2 = int(input("Inserisce il numero 2"))


res = solveMeFirst(num1,num2)

print(res)