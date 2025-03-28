# Esercizio funzioni
'''Del libro: Milagro'''

def greet_user():
    """Stampa un semplice saluto"""

    print("Hello")

greet_user()



def greet_user(username):
    print(f"Ciao, {username}")

greet_user("Mari")

# 8.1 

def display_message():
    print("In questo corso sto allenando tanto la ragione")

display_message()

# 8.2

def favorite_book(titolo):
    print(f"Uno dei miei libri favoriti è: {titolo}")

favorite_book("Speak")

# chiamata per posizione

def describe_mascota(tipo_animale, nome_mascota) -> str:
    print(f"\nYo tengo un {tipo_animale} que se llama {nome_mascota}")

describe_mascota("Caja", "Bender")

# chiamata per parola chiave

describe_mascota(nome_mascota="Gorro Frio", tipo_animale="Papagallo")

# Valori di default

def animal(nombre, tipo ="Perro", ):
    print(f"\n Tengo un {tipo}")
    print(f"Que se llama {nombre}")

animal("No me acuerdo") 
"""De esta manera, imprime el valor de Perro, porque esta definido de default y el nombre"""

animal("No seas bobita", "gata")
"""De esta manera, cambia el valor predefinido y en este caso, mete: gato"""

# retorno de un valor

def get_name(nombre, apellido) -> str:

    """Creo una variable que encadeno con el signo + e meto todo lo que me sirve"""
    # nombrecompleto = nombre + " " + apellido

    nombrecompleto = (f"{nombre} {apellido}")
    """Pero puedo tambien crear una variable formatada. Creo que es mas facil"""

    return nombrecompleto.title()


minombre = get_name("maritza", "figueroa")

print(minombre)