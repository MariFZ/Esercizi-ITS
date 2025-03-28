# ESERCIZIO 3

# Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero

# def countdown(n: int) -> int:
#     '''soluzione col ciclo while
#     Cosa dice:

#     mentre il valore di n sia maggiore o uguale a 0:

#         Quindi n può avere il valore di 5:
#             * 5 è maggiore di 0?: siiiiii
#                 stampo: 5
#                 diminuisco il valore di n
#                 5 -1 = 4
#             * 4 è maggiore di 0? : siiii
        
#         e cosi via
#     '''
#     while n >= 0:
#         print(n)
#         n= n -1

# print(countdown(5))

# # soluzione col ciclo For

# def countdown(n: int) -> int:

#     numeri_rovescia:list = []

#     for numero in range(n, -1, -1):
        # '''Attenzione: Ricordare questo:

        #     RANGE in Python accetta 3 argomenti separati da virgole:
            
        #     range(start, stop, step)

        #         start: da dove inizia
        #         stop: dove finisce
        #         step: l'incremento o decremento
            
        #         Quindi: (n,-1, -1) significa che genera numeri a partire da n fino a 0, scalando di -1

        #         n: il numero da cui partiamo
        #         -1: il numero a cui fermarsi (escluso), quindi ci fermiami a 0
        #         -1: passo negativo: diminuiamo di 1 ogni iterazione '''
        
#         numeri_rovescia.append(numero)
#         print(numero)
        
#     return numeri_rovescia
    
# print(countdown(5))


# print("-------------------------------------------")

# Esercizi

# Esegue un conto alla rovescia partendo da cinque e poi dice “Decollo!”

# n:int = 10

# while n > 0:
#     '''Con ciclo while'''
#     print(n)
#     n = n -1
# print(f"Sigla\n")


# # col ciclo For


# n:int = 15

# for numero in range(n, 0, -1): 
#     '''in questo caso non ho fatto n, -1 (che prende fino a 0)
#       sino che l'ho detto di arrivare fino a 1, per quello ho cambiato:
      
#       n: il valore da dove inizia
#       0: dove si ferma, quindi stampa fino a 1
#       -1: quanto deve saltare '''
    
#     print(numero)
# print("Iniziamo!!!")

while True:

    line = input('> ') # Questo chiede all'utente di inserire una linea/frase: stringa
    if line == 'done':
        break

print(line)
print('Done!')









































#     numeri: list = []

   
#     for numero in range (n, -1, -1):
#         numeri.append(numero)
#         print(numero)

#     return numeri


# print(countdown(5))


# # def countdown(n: int) -> int:

# #     numeri: list = []

#     # for numero in range (n, -1, -1):
#     for numero in range (n, -1, -1):
#         numeri.append(numero)
#         print(numero)

#     return numeri

# # # numero = 9
# print(countdown(5))



  

# parola: str= input("Inserisci la parola che desideri invertire: ")

# lunghuezza: int=(len(parola))

# parola_invertita: list[str]= []

# i: int = 0

# while i < lunghuezza:
#     lettera = parola[-(i + 1)]   # somma degli indici alla rovescia sino stampa sempre l'ultima parola. 
#     parola_invertita.append(lettera)
#     i += 1
# else:
#     print(f"La parola invertita è: {"" .join(parola_invertita)}")