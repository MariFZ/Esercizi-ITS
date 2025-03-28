# Esercizio 9
# Il valore di π può essere approssimato utilizzando la seguente serie infinita:

# π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

# Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari per ottenere approssimazioni sempre più accurate. 
# Quindi:

# progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
# modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
# modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
# modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.
# Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.


soglie = [3.14, 3.141, 3.1415, 3.14159]  
numeratore = 4

# 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 
for soglia in soglie:
    denominatore = 1  # primo numero dispari
    pi = 0            # pi come 0 valore approssimato)
    segno = 1          
    termini = 0  
    

    # differenza tra pi e la soglia con la tolleranza

    while round(pi - soglia,2):          # abs- calcola il valore assoluto di un numero, elimina il segno negativo
        pi += segno * (numeratore / denominatore)   # Somma o sottrai il termine
        segno *= -1                                 
        denominatore += 2                           
        termini += 1  
       
    print(f"Per ottenere {soglia} servono {termini} termini.")







# prima soluzione
# soglie = [3.14, 3.141, 3.1415, 3.14159]  
# numeratore = 4

# # 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 
# for soglia in soglie:
#     denominatore = 1  # primo numero dispari
#     pi = 0            # pi come 0 valore approssimato)
#     segno = 1          
#     termini = 0  
#     tolleranza = 0.00001  # Differenza accettabile per considerare i valori uguali

#     # differenza tra pi e la soglia con la tolleranza

#     while abs(pi - soglia) > tolleranza:          # abs- calcola il valore assoluto di un numero, elimina il segno negativo
#         pi += segno * (numeratore / denominatore)   # Somma o sottrai il termine
#         segno *= -1                                 
#         denominatore += 2                           
#         termini += 1                

#     print(f"Per ottenere {soglia} servono {termini} termini.")

# SECONDA SOLUZIONE prf.  Giorgi

# def serie(target: str= "3.14159"):

#     pi: float = 0.0
#     segno: int = 1
#     denominatore: int = 1
#     contatore: int = 0
#     # pi_value = []

#     while True:

#         # print(f"{pi=}){segno=} {denominatore=}{contatore=}")
#         pi += segno* (4/ denominatore)

#         # pi.value.append(pi)

#         if str(pi)[:len(target)] == target:

#             print(f"La serie converge a {pi} dopo {contatore} iterazioni")

#             break

#         segno *= -1
#         denominatore += 2
#         contatore += 1

#         # return pi_value
    

# serie()










