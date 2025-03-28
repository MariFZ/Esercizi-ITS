# 3.6 PIU OSPITI

invitati: list=["Andrew", "Chiara", "Jean Paul"]

print("Ciao " + invitati[0] + "," + invitati[1] + ", " + invitati[2] + ", " + "come sapete siete invitati a cena. Abbiamo appena saputo che abbiamo un tavolo più grande" )


invitati.insert(0,"David")
print(invitati)

# IN QUESTO CASO POTEVO USARE ANCHE LEN PER SAPERE LA LUNGUENZA DELLA LISTA

# invitati.insert(len(invitati)//2,"Federica")

invitati.insert(2,"Federica")
print(invitati)

invitati.append("Paola")
print(invitati)

print("Ciao " + invitati[0] + ", ancora non ci conosciamo personalmente, vuoi venire a cena?")

print("Ciao " + invitati[1] + ", da tanti anni non ci vediamo, vuoi venire a cena?")

print("Ciao " + invitati[2] + ", sono in debito con te da tante cose, vuoi venire a cena?")

print("Ciao " + invitati[3] + ", non abbiamo avuto tempo di salutarci, vuoi venire a cena?")

print("Ciao " + invitati[4] + ", sono in debito con te da tante cose, vuoi venire a cena?")

print("Ciao " + invitati[5] + ", non abbiamo avuto tempo di salutarci, vuoi venire a cena?")

print(invitati)