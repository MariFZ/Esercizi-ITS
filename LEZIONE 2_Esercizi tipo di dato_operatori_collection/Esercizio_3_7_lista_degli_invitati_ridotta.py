# 3.7 LISTA DEGLI INVITATI RIDOTTA

invitati: list[str]=['David', 'Andrew', 'Federica', 'Chiara', 'Jean Paul', 'Paola']

messaggio: str=("Ciao, purtroppo il tavolo non arriverà in tempo e quindi abbiamo spazio solo per 2 persone")

print(messaggio)
print(invitati)

# RICORDARE: Potevo fare anche pop() che elimina l'ultimo della lista a prescindere di chi voglio elimninare

invitati.pop(1)
print("Ciao " + invitati[1] + " purtroppo questa volta non possiamo averti tra noi")
print(invitati)


invitati.pop(3)
print("Ciao " + invitati[3] + " purtroppo questa volta non possiamo averti tra noi")
print(invitati)


invitati.pop(0)
print("Ciao " + invitati[0] + " purtroppo questa volta non possiamo averti tra noi")
print(invitati)

invitati.pop(0)
print("Ciao " + invitati[0] + " purtroppo questa volta non possiamo averti tra noi")
print(invitati)
#print(invitati)

print("Ciao " + invitati[0] + "," + invitati [1] + " siamo felici di avervi tra noi")

# uso di del per cancellare tutto

del invitati [0] 
print(invitati)

del invitati [0] 
print(invitati)
