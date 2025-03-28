# 2.4 CASI DI NOMI

nome = str("Paulina")


# IN ALTRI CASI SI SONO CREATE VARIE VARIBILI


print("Ecco il tuo nome " + nome  + " in maiuscola: " + nome.upper() + " \nAdesso tutto in minuscolo: " + nome.lower() + "\ne per ultimo, tutto in titolo: " + nome.title())


print(f"Ecco il tuo nome {nome}  in maiuscola:  {nome.upper()}   \n Adesso tuo nome in minuscola: {nome.lower()}  \n e per ultimo, il tuo nome tutto in titolo: {nome.title()}")

# LOWER E UPPER è utile quando devo comparare i valori inseriti dall'utente

# POTEVO ANCHE CREARE DELLE VARIABILI COSI: 

nome = str("Paulina")
lowercase = nome.lower()
uppercase = nome.upper()
titlecase = nome.title()