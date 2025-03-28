import random


print("'BANG !!!!! AND THEY'RE OFF !!!!!'")


def posizione_gara(pos_tartaruga:int, pos_lepre:int):
    pos_tartaruga = 1
    pos_lepre = 1

    return pos_tartaruga, pos_lepre


def mossa_tartaruga(pos_tartaruga:int):
    possibile_mossa = random.randint(1,10)
  
    # passo veloce tartaruga
    if possibile_mossa > 1 or possibile_mossa > 5:
        pos_tartaruga +=  3  # passo veloce
        pos_tartaruga

    elif possibile_mossa > 6 or possibile_mossa > 7:
        # sciovolata tartaruga
        pos_tartaruga -= -6
        if pos_tartaruga < 1:
            posizione_gara(pos_tartaruga)
       
    elif possibile_mossa > 8 or possibile_mossa > 10:
        # passo lento
        pos_tartaruga = 1 

    else:
        pos_tartaruga += 1

    return pos_tartaruga


# prova mossa tartaruga

pos_tartaruga = 1


while pos_tartaruga in range(10):

    pos_tartaruga = mossa_tartaruga(pos_tartaruga)
    print(f"Cosi va la tartaruga: {pos_tartaruga}")


def mossa_lepre(pos_lepre:int):
    possibile_mossa = random.randint(1,10)
  
    # riposo
    if possibile_mossa > 1 or possibile_mossa > 2:
        pos_lepre =  0  # non si muove
        

    if possibile_mossa > 3 or possibile_mossa > 4:
        # grande balso
        pos_lepra += 9

    elif possibile_mossa > 5 or possibile_mossa > 5:
        # grande sciovolata
        pos_lepre -= 12
        if pos_lepre < 1:
            posizione_gara(pos_lepre)
    
    elif possibile_mossa > 6 or possibile_mossa > 8:
        # piccolo balzo
        pos_tartaruga += 1
    
    else:
        pos_lepre < 1
        posizione_gara(pos_lepre)

        pos_tartaruga -= 2

    return pos_lepre

# prova mossa lepre

pos_lepre = 1


while pos_lepre in range(10):

    pos_lepre = mossa_tartaruga(pos_lepre)
    print(f"Cosi va la lepre: {pos_lepre}")




# i = 1 # contatore per i secondi

# while randint (i, 70):

#     if pos_tartaruga <= 69 or pos_lepre <= 69:
    
#         if pos_tartaruga < 0:

#       
    



    





    

    




    
    








