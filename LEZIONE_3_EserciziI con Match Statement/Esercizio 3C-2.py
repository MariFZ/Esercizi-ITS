# Esercizio 3C-2. Scrivere un programma in Python che:
# converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
# Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero
# e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

# - 106-110 → 4.0
# - 101-105 → 3.7
# - 96-100 → 3.3
# - 91-95 → 3.0
# - 86-90 → 2.7
# - 81-85 → 2.3
# - 76-80 → 2.0
# - 70-75 → 1.7
# - 66-69 → 1.0
# Altro caso → "Voto non valido"

# voto: int =int in range(66,110("Inserisci il voto di laurea: "))

voto: int =int(input("Inserisci il voto di laurea: "))

# voto: list[int] = [110,]

match voto:
    
    
        case voto if 106 <= voto <= 110:
            print(f"Il tuo voto: {voto} nel sistema americano è: GPA 4.0")
    
        case voto if 101< voto <=115:
            print(f"Il tuo voto: {voto} nel sistema americano è: GPA 3.7")
    
        case voto if 96 <= voto <=100:
            print(f"Il tuo voto: {voto} nel sistema americano è: GPA 3.3")
    
        case voto if 91<= voto >=95:
            print(f"Il tuo voto: {voto} nel sistema americano è: GPA 3.7")
    
        case voto if 86<= voto <=90:
            print(f"Il tuo voto: {voto} nel sistema americano è: GPA 2.7")
    
        case voto if 81 <= voto <= 85:
            print(f"Il tuo voto: {voto} nel sistema americano è: GPA 2.3")
    
        case voto if 76 <= voto <= 80:
            print(f"Il tuo voto: {voto} nel sistema americano è: GPA 2.0")

        case voto if 70<= voto <=75:
            print(f"Il tuo voto: {voto} nel sistema americano è: GPA 1.7")

        case voto if 66 <= voto <=69:
            print(f"Il tuo voto: {voto} nel sistema americano è: GPA 1.0")

        case _:
            print(f"Il tuo voto: {voto} nel sistema americano non è valido")

