# ESERCIZIO 4.1

# Pensate ad almeno tre tipi di pizza preferiti. Memorizzate i nomi delle pizze in un elenco e poi utilizzate un ciclo for per stampare il nome di ciascuna pizza. 
# Modificate il ciclo for per stampare una frase con il nome della pizza, invece di stampare solo il nome della pizza. 
# Per ogni pizza, dovreste avere una riga di output contenente una semplice affermazione come "Mi piace la pizza al salame".
# Aggiungete una riga alla fine del programma, al di fuori del ciclo for, che indichi quanto vi piace la pizza. 
# L'output dovrebbe essere composto da tre o più righe sui tipi di pizza che vi piacciono e poi da una frase aggiuntiva, come ad esempio: "Adoro la pizza!


# lista

pizze: list[str]=["gorgozzola e mele", "quatro formaggi", "caprese"] 

# ciclo for stampando il nome di ciascuna pizza

for pizza in pizze:
    print(pizza)

# Stampa frase insieme al nome della pizza

for pizza in pizze:
    print(f"Che buona la pizza: {pizza}")

# Output fuori del ciclo tre o più righe sui tipi di pizza che vi piacciono e frase aggiuntiva, come ad esempio: "Adoro la pizza!

print(f"Questo è l'elenco delle pizze che mi piaciono: \n Questa è la migliore: {pizze[0]} \n Anche questa pizza: {pizze[1]}, mi piace molto! \n E quest'ultima: {pizze[2]} quando voglio cambiare. \nQuanto mi piace la pizza!")
    
    
    #print(f"Che buona la pizza: {pizza}")

    # aggiunta affermazione

# seconda possibilità

# for i in range(0,len(pizze)):
#     print(f"Questa pizza è anche buona: {pizze[i]}")



# for pizza in pizze:
#     if pizza == "gorgonzola e mele":
#         print(f"Questa è la mia pizza favorita: {pizze[0]}!")

#     if pizza == "quatro formaggi":
#         print(f"Anche questa pizza mi piace molto: {pizze[1]}!")
    
#     if pizza == "caprese":
#         print(f"E per ultimo, va anche bene questa pizza:{pizze[1]}!")


# print(f"Quanto mi piace la pizza! {' ,' .join(pizze)}")

