# Esercizio 4
# Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). 
# L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.
# Il programma deve:
# 1. Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
# 2. Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).


 # inizializzo le variabili

primo_numero = float(input("Inserisci il primo numero positivo: "))

max_numero = primo_numero   # do un valore alla variabile max_numero
min_numero = primo_numero   # do lo stesso valore alla variabile min_numero
somma = 0
media = 1
conta_interi= 0            # contatore dei numeri interi

while True:
    numero:float = float(input("Inserisce ancora un numero: "))

    if numero < 0:
        print(f"Programma terminato, hai inserito un numero negativo\n")
        break

    # se invece il numero è positivo
    else:
       
        if numero.is_integer():             # funzione che verifica se il numero è intero
            somma += numero
            conta_interi += 1
                
        if numero > max_numero:
            max_numero = numero

        elif numero < min_numero:
            min_numero = numero

if conta_interi > 0:
    media = somma/conta_interi
    print(f"La media dei numeri interi inseriti è: {media:.2f}") 

print(f"Il numero massimo che hai inserito è: {max_numero} e il minimo numero è: {min_numero}")
        
        
      
           
 


# soluzione presenta ----Da migliorare, non segue esattamente la traccia

# '''La soluzione presenta alcuni errori:

#     1. Quando l'utente scrive un numero negativo, 
#     doveva fermarsi non continuare a chiedere'''

# # verifico che il numero sia positivo. La richiesta continua finchè non viene scritto il numero positivo
# while True:
#     primo_numero = float(input("Inserisci il primo numero positivo: "))

#     if primo_numero < 0:
#         print(f"Hai inserito un numero negativo, riprova ancora")
#         continue

#     elif primo_numero > 0: 

#     # inizializzo le variabili

#         '''Secondo errore: 
#             Il contatore mi serviva solo per i numeri interi
#             nel mio caso, era di tutti'''

#         max_numero = primo_numero   # do un valore alla variabile max_numero
#         min_numero = primo_numero   # do lo stesso valore alla variabile min_numero
#         somma = 0
#         media = 0
#         i= 1                        # contatore delle iterazioni, mi serve per fare la media dei numeri interi
   
#    # ripeto l'azione finchè non si scrive un numero negativo
   
#     while True: 
    
#         number = float(input("Inserisci ancora un numero: "))   # con float, la variabile accetta anche i numeri interi (gli trasforma in decimali)
        
#         if number > 0: 
#             if number.is_integer():             # funzione che verifica se il numero è intero
#                 somma += number
#                 media = somma + number/ i 
                
#                 if max_numero < number:
#                     max_numero = number
#                 elif min_numero > number:
#                     min_numero = number
#             else:
#                 if max_numero < number:
#                     max_numero = number
#                 elif min_numero > number:
#                     min_numero = number
#             i+=1
#             continue
        
#         # fermo l'inserimento dei numeri perchè negativo
#         break                                   
#     print("Hai inserito un numero negativo")

# # si ferma tutto il ciclo e si stampa la media e in numero massimo e minimo 

#     break                                       
# print(f"La media dei numeri è: {media}, il numero piu grande è: {max_numero} e il numero piu piccolo è: {min_numero}")