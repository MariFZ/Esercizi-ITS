# ESERCICIO Match Statement e condizioni
# IF and AND
    # Se il numero è positivo e pari
    # Se il numero è positivo e dispari
    # Se il numero è negativo e pari
    # Se il numero è negativo e dispari

numero: int = int(input("Inserisci un numero: "))

match numero: 

        case numero if numero > 0 and numero%2==0:
            print(f"{numero} is positive and even")
        
        case numero if numero > 0 and numero!=0:
            print(f"{numero} is positive and odd")
        
        case numero if numero > 0 and numero%2==0:
            print(f"{numero} is negative and even")
        
        case numero if numero < 0 and numero!=2:
            print(f"{numero} is negative and odd")
        
        case _:
            print(f"The number is zero")

# FORMA CON IF/ELIF/ELSE

# if numero > 0 and numero%2==0:
#     print(f"{numero} is positive and even")

# elif numero > 0 and numero%2!=0:
#     print(f"{numero} is positive and odd")

# elif numero < 0 and numero%2==0:
#     print(f"{numero} is negative and even")

# elif numero numero < 0 and numero%2!=0:
#     print(f"{numero} is negative and odd")

# else:
# print(f"The number is zero")
        


