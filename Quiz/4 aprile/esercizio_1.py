# esercizio 1

# Nel gioco del Blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. Ogni carta ha un valore compreso tra 2 e 11 inclusi.

# Il valore numerico delle carte (da 2 a 10) è equivalente al loro valore nominale.
# Le figure (Jack, Regina, Re) non sono incluse in questo esercizio e vengono ignorate.
# L'Asso (valore 11) può valere 1 o 11, a seconda di quale sia più favorevole al giocatore:
# Se la somma della mano supera 21, e c'è almeno un asso valutato 11, quell'asso deve essere considerato 1 per evitare il "bust" (superare 21).
# Scrivi una funzione che prende in input una lista di interi rappresentanti i valori delle carte e restituisce il valore totale della mano secondo le regole del Blackjack.

#print(blackjack_hand_total([1, 10, 11]))


def blackjack_hand_total(card: list[int]) -> int:
    
    somma = sum(card)
  
    if somma > 21:
        somma -=10
      
    return somma

        
print(blackjack_hand_total([1, 10, 11]))
        
























# def blackjack_hand_total(card: list[int]) -> int:
#     somma = 0
#     assi = 0
    
#     for i in card:
#         if i == 1:  # Se l'elemento è un asso, incrementiamo il contatore
#             assi += 1
#         elif i > 10:  # Se l'elemento è una figura (J, Q, K), aggiungiamo 10
#             somma += 10
#         else:
#             somma += i  # Somma tutte le altre carte normalmente

#     # Tratta gli assi come 11 finché non supera 21
#     for _ in range(assi):
#         if somma + 11 <= 21:
#             somma += 11  # L'asso viene trattato come 11
#         else:
#             somma += 1  # Se la somma supera 21, trattiamo l'asso come 1

#     return somma


   
   
    
        
# # print(blackjack_hand_total([2, 3, 5]))
# # print(blackjack_hand_total([11, 5, 5]))
# print(blackjack_hand_total([1, 10, 11]))