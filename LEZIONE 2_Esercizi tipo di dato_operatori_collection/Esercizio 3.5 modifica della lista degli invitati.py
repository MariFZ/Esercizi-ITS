# 3.5 MODIFICA DELLA LISTA DEGLI INVITATI

invitati: list[str]=["Andrew", "Chiara", "Jean Paul"]


print("Ciao " + invitati[0] + ", " + invitati[2]  + ", da tanti anni non ci vediamo. Volete venire a cena?.  Anche " + invitati[1] + " voleva venire, ma purtroppo ha un impegno"  )


# ospite che non può venire 

invitati.remove("Chiara")

"Chiara" in invitati


# agregar nuova persona in lista.  Potevo anche assegnare all'indice il nome della persona

#invitati.append("Sandra")

invitati[1] = "Sandra"



# print nuovi messaggi

print("Ciao " + invitati[0] + ", da tanti anni non ci vediamo, vuoi venire a cena?")

print("Ciao " + invitati[1] + ", sono in debito con te da tante cose, vuoi venire a cena?")

print("Ciao " + invitati[2] + ", non abbiamo avuto tempo di salutarci, vuoi venire a cena?")





