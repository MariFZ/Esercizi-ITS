# FUNZIONI SENZA RITORNARE UN VALORE

# def greet(name:str) -> None: 


#     print(f"Hello {name}!")
    
# greet("Angela")
# greet("Mari")

#  FUNZIONE CON RETURN

def greet(name: str) -> str:
    return f"Hello {name}!"

messaggio1 = greet("Angela")

messaggio2 = greet("Mari")

print(messaggio1)  # Ora possiamo riutilizzare il valore
print(messaggio2)  # Ora possiamo riutilizzare il valore


