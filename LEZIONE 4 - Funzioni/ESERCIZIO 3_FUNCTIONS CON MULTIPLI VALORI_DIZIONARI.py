# ESERCIZIO 4 - FUNCTIONS CON MULTIPLI VALORI - DIZIONARI

def user(myname: str, myrole: str) -> dict[str,str]:  # qui devo inserire il valore che cambierà

    return{"name":myname, "role": myrole}

usuari = user("Alice","Boss")

print(f"Questi sono i nomi e ruoli: {usuari["name"]}, {usuari["role"]}")
