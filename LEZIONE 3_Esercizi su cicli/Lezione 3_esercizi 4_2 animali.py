# ESERCIZIO 4.2

# 4-2. Animali:
# Pensate ad almeno tre animali diversi che abbiano una caratteristica comune. 
# 1. Memorizzate i nomi di questi animali in un elenco e poi utilizzate un ciclo for per stampare il nome di ogni animale.
# 2. Modificate il vostro programma per stampare un'affermazione su ogni animale, ad esempio Un cane sarebbe un ottimo animale 
# 3. Aggiungete una riga alla fine del programma, indicando ciò che questi animali hanno in comune. 
# Si potrebbe stampare una frase come "Ognuno di questi animali sarebbe un ottimo animale domestico!

animali: list[str] =["leone", "giraffa", "elefante"]


# 1. elenco animali comuni e stampa il nome di ogni animale

for animale in animali:
    print(f"Ecco alcuni animali della giungla: {animale}")

# 2. Affermazione su ogni animale 
for animale in animali:
    if animale == "leone":
        print(f"Il \"{animali[0]}\" è il Re della giungla!")

    if animale == "giraffa":
        print(f"La \"{animali[1]}\" ha il collo molto lungo!")
    
    if animale == "elefante":
        print(f"\"L'{animali[2]}\" deve essere molto pesante!")


# 3. Cosa hanno in comune

print(f"Questi animali: \"{', ' .join(animali)}\" vivono nelle giungle di alcuni paesi dell'Africa!")


