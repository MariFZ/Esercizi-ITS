import random


print("==================================")

print("'BANG !!!!! AND THEY'RE OFF !!!!!'")

print("==================================")


def posizione_gara_tartaruga():
    '''posizione iniziale degli animali, cancelli di partenza'''

    pos_tartaruga = 1
    return pos_tartaruga

def posizione_gara_lepre():
    '''posizione iniziale degli animali, cancelli di partenza'''

    pos_lepre = 1
    return pos_lepre


def mossa_tartaruga(pos_tartaruga:int):
    possibile_mossa_tartaruga = random.randint(1,10)
    '''variabile che prenderà il numero aleatorio tra 1 a 10 che farà
    dopo il match con i diversi casi di movimento della tartaruga'''

    match possibile_mossa_tartaruga:
        case possibile_mossa_tartaruga if 1 <= possibile_mossa_tartaruga <= 5: # passo veloce 50%
            pos_tartaruga +=  3  

        case 6|7: # sciovolata 20%
            pos_tartaruga -= 6
            if pos_tartaruga < 1:
                pos_tartaruga = posizione_gara_tartaruga()

        case possibile_mossa_tartaruga if 8 <=possibile_mossa_tartaruga <=10: # passo lento 30%
            pos_tartaruga +=1
    
    return pos_tartaruga


# print(f"\nPosizione iniziale TARTARUGA: {posizione_gara_tartaruga()}") # richiamo la funzione che ha il parametro di defaul di partenza = 1

# posizione_gioco_tartaruga = posizione_gara_tartaruga()

# for i in range(30): # verifica che effettivamente le funzioni di movimento funzionano per la tartaruga
#     posizione_gioco_tartaruga = mossa_tartaruga(posizione_gioco_tartaruga)
#     print(f"Al giro {i+1} questa è la posizione della tartaruga: {posizione_gioco_tartaruga}")


def mossa_lepre(pos_lepre:int): 
    possibile_mossa_lepre = random.randint(1,10)
    '''variabile che prenderà il numero aleatorio tra 1 e 10 per fare il movimento della lepre
    secondo i diversi movimenti'''

    match possibile_mossa_lepre:

        case 1|2:  # riposo non si muove 20% 
            pos_lepre = pos_lepre

        case 3|4: # grande blazo 20%
            pos_lepre +=9

        case 5:  # grande sciovolata 10%
            pos_lepre -= 12
            if pos_lepre < 1:
                pos_lepre = posizione_gara_lepre()
        
        case possibile_mossa_lepre if 6 <= possibile_mossa_lepre == 8: # piccolo balzo 30%
            pos_lepre += 1
        
        case 9|10: # piccola sciovolata
            pos_lepre -= 2
            if pos_lepre < 1:
                pos_lepre = posizione_gara_lepre()
    
    return pos_lepre

# print(f"\nPosizione iniziale LEPRE: {posizione_gara_lepre()}") # stampo la prima posizione che è legata alla  funzione di default = 1

# # creo una variabile conterà tutte le posizioni della lepre durante il gioco
# posizione_gioco_lepre = posizione_gara_lepre() # richiamo la funzione che di default la posizione è sempre 1

# # Controllo che la funzione mossa funzione
# # for giro in range(30): # verifica il movimento della funzione mossa lepre
# #     posizione_gioco_lepre = mossa_lepre(posizione_gioco_lepre)
# #     print(f"Al giro {giro+1}: la lepre è alla posizione {posizione_gioco_lepre}")


def fattori_ambientali(pos_tartaruga, pos_lepre, orologio):

    pos_tartaruga = mossa_tartaruga(pos_tartaruga)
    pos_lepre = mossa_lepre(pos_lepre)
    
    if orologio % 10 == 0:

        sceglie_temperatura = random.choice(["pioggia", "sole"])
    
        match sceglie_temperatura:

            case 'pioggia':
                print(f"Purtroppo il tempo è cambiato al giro {orologio} e ci saranno delle penalità per entrambi concorrenti")
                pos_tartaruga += -1 # penalità per la tartaruga
                print(f"La tartaruga che era in posizione: {pos_tartaruga} perde 1 quadrante!")
                pos_lepre -= 2
                print(f"La lepre che era in posizione: {pos_lepre} perde 2 quadranti!")

            case 'sole':
                print(f"Adesso invece al giro {orologio} è uscito il sole!")
                # pos_tartaruga = pos_tartaruga
                # print(f"La tartaruga rimane nella sua posizione: {pos_tartaruga}")

    return pos_tartaruga, pos_lepre


# inizio col ciclo while perchè devo ripeterla un numero indeterminato



pos_tartaruga = 1  # variabile che conterà le posizioni della tartaruga
pos_lepre = 1      # variabile che conterà le posizioni della leère
orologio:int = 1   # conterà l'interazioni'''
quandranti:list[int] = range(1,71)


from test_lista_con_underscore import da_numero_a_punto


# while mossa_tartaruga(pos_tartaruga) < 71 or mossa_lepre(pos_lepre) < 71: # 
while pos_tartaruga < 71 or pos_lepre < 71: # 
    
    fattori_ambientali(pos_tartaruga, pos_lepre, orologio)
    print(da_numero_a_punto(quandranti,pos_tartaruga, pos_lepre))

    pos_tartaruga = mossa_tartaruga(pos_tartaruga)
    '''aggiorna la posizione della tartaruga ad ogni ciclo'''
    pos_lepre = mossa_lepre(pos_lepre)
    '''aggiorna la posizione della lepre ad ogni ciclo'''

    
    print(f"\n")
       
    if  pos_tartaruga == pos_lepre:
        print("Pareggio!! Forza!!")
        
    elif pos_tartaruga > 71:
        print("Evviva! TORTOISE WINS|| VAY")
        break
        
    elif pos_lepre > 71:
        print("Evviva! HARE WINS|| YUCH!")
        break
        
    else:
        print(f"Gara ancora in corso. Siamo al giro: {orologio}")

        #richiamo la funzione se l'orologio è a 10 o 20
        orologio += 1
        
        print(f"\nCosi vanno le posizioni dei nostri concorrenti:\nTARTARUGA: {pos_tartaruga} \nLEPRE: {pos_lepre}\n\n")
        print(da_numero_a_punto(quandranti,pos_tartaruga, pos_lepre))



print(f"La gara si è vinta dopo {orologio} giri")






             
        



    





    

    




    
    








