# ESERCIZIO 4 : Match Statement and variables

# ESEMPIO CON VALORI FISSI
genere: str= "f"
age: int= 5


match (genere, age):

    case ("f", 5):
        print("Piccola!")
    case ("m", 5):
        print("Piccolo!")
    case ("f", 10):
        print("Grande!")
    case ("m", 10):
        print("Gigante!")
    case _:
        print("Kinder Sorpresa!")

# ESEMPIO CON VALORI IN INPUT87

age: int= int(input("Scrive la tua età: "))
genere: str = input("Digitare 'm' per maschio e 'f' per femmina: (m/f)")


match (genere, age):

    case ("f", 5):
        print("Piccola!")

    case ("m", 5):
        print("Piccolo!")

    case ("f", 10):
        print("Grande!")

    case ("m", 10):
        print("Gigante!")

    case _:
        print("Kinder Sorpresa, sei anziano ;)!")