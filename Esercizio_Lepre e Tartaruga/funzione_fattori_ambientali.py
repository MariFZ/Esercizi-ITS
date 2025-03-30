# import random

def fattori_ambientali(orologio):

    if orologio % 10 == 0:

        # sceglie_temperatura = random.choice("pioggia", "sole")
    

        match sceglie_temperatura:

            case 'pioggia':
                print(f"Purtroppo il tempo è cambiato al giro {orologio} e ci saranno delle penalità per entrambi concorrenti")
                pos_tartaruga += -1 # penalità per la tartaruga
                print(f"La tartaruga che era in posizione: {pos_tartaruga} perde 1 quadrante!")
                pos_lepre -= 2
                print(f"La lepre che era in posizione: {pos_lepre} perde 2 quadranti!")

            case 'sole':
                print(f"Adesso invece al giro {orologio} è uscito il sole!")
                pos_tartaruga = pos_tartaruga
                print(f"La tartaruga rimane nella sua posizione: {pos_tartaruga}")
                pos_lepre = pos_lepre

    return pos_tartaruga, pos_lepre

if __name__== "__main__":
    fattori_ambientali()


