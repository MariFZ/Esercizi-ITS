# Esercizio 3C-10. 
# Scrivere un programma che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), 
# salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

# - Capodanno → 1 Gennaio → "Capodanno"
# - San Valentino → 14 Febbraio → "San Valentino"
# - Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
# - Ferragosto → 15 Agosto → "Ferragosto"
# - Halloween → 31 Ottobre → "Halloween"
# - Natale → 25 Dicembre → "Natale"
# - Altro caso → "Nessuna festività importante in questa data."

# Expected Output:

# Inserisci il giorno: 25
# Inserisci il mese: 12
# Output: Il 25/12 è Natale!

# - - - - - - - - - - - - - - -

# Inserisci il giorno: 5
# Inserisci il mese: 3

# giorno: int = int(input("Inserisci il giorno: "))
# mese: int = int(input("Inserisci il mese: "))

# feste: tuple[int] = ()

# convert_feste: list[int] = list(feste)  # convertiamo la tupla in lista

# convert_feste.append(giorno)
# convert_feste.append(mese)


# match convert_feste:

#     # Capodanno → 1 Gennaio → "Capodanno"

#     case (1,1):
#         print(f"Il {giorno}/{mese} è Capodanno")
    
#    # San Valentino → 14 Febbraio → "San Valentino"
    
#     case (14,2):
#         print(f"Il {giorno}/{mese} è San Valentino")

#     # Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"

#     case (25,6):
#         print(f"Il {giorno}/{mese} è la Festa della Repubblica Italiana")
    
#     # 15 Agosto → "Ferragosto

#     case (15,8):
#         print(f"Il {giorno}/{mese} è Ferragosto")

#     # Halloween → 31 Ottobre → "Halloween"
    
#     case (31,10):
#         print(f"Il {giorno}/{mese} è Halloween")
    
#     # Natale → 25 Dicembre → "Natale"
    
#     case (25,12):
#         print(f"Il {giorno}/{mese} è Natale")
    
#     case _:
#         print("Nessuna festività importante in questa data.")

# SECONDA POSSIBILITA'

giorno_user: int = int(input("Inserisci il giorno: "))
mese_user: int = int(input("Inserisci il mese: "))

if not giorno_user.isdecimal() or not mese_user.isdecimal():
    print("Inserire un valore intero per il giorno e per il mese! ")

giorno, mese = int(giorno_user), int(mese_user)

# Definisci la tupla con la data

feste: tuple[int] = (giorno, mese)

giorni_per_mese: list[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


match feste:
    
    case (giorno, mese) if giorno <= 0 or mese <= 0:
        print("Inserire un valore positivo per il giorno e per il mese")
    # Capodanno → 1 Gennaio → "Capodanno"

    case (1,1):
        print(f"Il {giorno}/{mese} è Capodanno")
    
   # San Valentino → 14 Febbraio → "San Valentino"
    
    case (14,2):
        print(f"Il {giorno}/{mese} è San Valentino")

    # Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"

    case (25,6):
        print(f"Il {giorno}/{mese} è la Festa della Repubblica Italiana")
    
    # 15 Agosto → "Ferragosto

    case (15,8):
        print(f"Il {giorno}/{mese} è Ferragosto")

    # Halloween → 31 Ottobre → "Halloween"
    
    case (31,10):
        print(f"Il {giorno}/{mese} è Halloween")
    
    # Natale → 25 Dicembre → "Natale"
    
    case (25,12):
        print(f"Il {giorno}/{mese} è Natale")

    case (giorno,mese) if mese > 12 or giorno > giorni_per_mese[m-1]:
        print(f"Il {giorno}/{mese} non esiste")
    
    case _:
        print("Nessuna festività importante in questa data.")

    

    


    



