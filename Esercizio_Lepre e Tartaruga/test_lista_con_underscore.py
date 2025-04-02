def da_numero_a_punto(quadranti:list[int], pos_tartaruga:int, pos_lepre:int):
    
    lista_posizioni:list = []
  
    for number in quadranti:

        if number == pos_tartaruga and number == pos_lepre:
            lista_posizioni.append("OUCH")
        elif number == pos_tartaruga:
            lista_posizioni.append("T")
        elif number == pos_lepre:
            lista_posizioni.append("H")
        else:
            lista_posizioni.append('_'*number)

    return lista_posizioni

# pos_tartaruga = 10
# pos_lepre = 10
# lista1 = list(range(1,71))
# '''la sintassi per creare una lista da un punto ad un'altro'''

# print(da_numero_a_punto(lista1,pos_tartaruga, pos_lepre))
#     #   e dopo la funzione con gli argomenti
# da_numero_a_punto (quadranti:list[int], pos_tartaruga:int, pos_lepre:int):


if __name__== "__main__": 




# # spiegazione tra l'uso di range nel ciclo for e dentro una lista
# for number in range(1, 6):
#     ''''non è una lista, stampa semplicemente
#     i numeri da 1 a 5'''
#     print(number)

# # se voglio creare una lista che prenda un range di numeri devo
# '''
# *trasformare il range in lista dentro la variabile che è una lista:

# lista:list[int] = list(range(a,b))

# spiegazione perchè NON dovevo scrive None nella funzione:

    '''ATTENZIONE: 
Quando la funzione è chiamata, pos_tartaruga e pos_lepre riceveranno i valori che gli passi. 
Per esempio: pos_tartaruga: 45, pos_lepre: 3
Se imposto None nella funzione, come ho fatto prima, quando la funzione viene richiamata, non avrà più i valori
# pos_tartaruga = None  
# pos_lepre = None
Ma subito dopo, tu imposti questi parametri a None, quindi non avrai più il valore originale che hai passato.
'''


