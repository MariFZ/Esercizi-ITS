# Esercizi per i diagrammi

# ESERCIZIO 2
# Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente

massimo = 0
i = 0

while i < 4:
    numero = int(input("Inserisci un numero positivo: "))
    if numero > massimo:
        massimo = numero
    i += 1
print(f"Il numero massimo è {massimo}")


# 3. Calcolo della somma di numeri positivi
# Progettare un algoritmo che calcoli la somma dei soli numeri positivi tra 5 valori inseriti dall'utente. 
# Quindi, se un numero è negativo o zero, ignora quel valore nella somma

somma = 0
i = 0


while i < 5:  # Fino a quando non abbiamo 5 numeri positivi
    numero = int(input("Inserisci un numero positivo: "))
    
    if numero > 0:  # Controlliamo che il numero sia positivo
        somma += numero
        i = i + 1  # Incrementiamo il contatore
    else:
        print("Il numero è 0 o negativo, riprova.")

print(f"La somma dei 5 numeri positivi è: {somma}")

# 4. Controllo della parità di un numero
# Progetta un algoritmo utile a determinare se un numero inserito dall'utente è pari o dispari.

numero = int(input("Inserisci un numero: "))

# Controlliamo se il numero è pari o dispari
if numero % 2 == 0:
    print(f"Il numero {numero} è pari.")
else:
    print(f"Il numero {numero} è dispari.")

    
# 5 Verifica se un numero è primo
# Progetta un algoritmo per determinare se un numero intero positivo inserito dall'utente è un numero primo

div = 2

numero = int(input("Inserisci un numero: "))

while div > 2:
     numero % 1==0: 
    div += 1 



# 7. Progetta un algoritmo che dati 10 numeri forniti dall'utente, conta quanti sono pari e quanti dispari.

numero_massimo = 10
contatore = 0 

print(f"Hai la possibilità di inserire un massimo di {numero_massimo} numeri")

while contatore < numero_massimo:
    numero = int(input(f"Inserisci un numero (tentativo {contatore + 1}/{numero_massimo}): "))
    if numero % 2 == 0:
        print(f"Il numero {numero_massimo} è pari.")
    else:
        print(f"Il numero {numero} è dispari.")
    
print("Hai terminato i tentativi. Grazie!")


# 8. Progetta un algoritmo che dati 7 numeri, trova e comunica i numeri maggiori di un valore soglia fornito dall'utente

# facciamo un list comprehesion 

def trova_numeri_maggiori_di_soglia(numeri, soglia):
    risultati = [numero for numero in numeri if numero > soglia]
    return risultati

# si poteva definire anche cosi: 
# 
# def trova_numeri_maggiori_di_soglia(numeri, soglia):
  #  risultati = []
   # for numero in numeri:
    #    if numero > soglia:
     #       risultati.append(numero)
    # return risultati

def main():
    numeri = []
    print("Inserisci 7 numeri:")
    for i in range(7):
        numero = int(input(f"Inserisci il numero {i + 1}: "))
        numeri.append(numero)
    
    soglia = int(input("Inserisci il valore soglia: "))
    
    risultati = trova_numeri_maggiori_di_soglia(numeri, soglia)
    
    print(f"I numeri maggiori della soglia {soglia} sono:")
    if not risultati:
        print("Nessun numero supera la soglia.")
    else:
        for numero in risultati:
            print(numero)

if __name__ == "__main__":
    main()

# Richiede reddito familiare e media dei voti, se il reddito è inferiore a 20.000 € e la media è superiore a 27 approva la borsa di studio, altrimenti rifiuta la richiesta visualizzando la motivazione

reddito = float(input("Inserisce il reddito familiare in questo formato, per esempio: 40000 (€):"))
voti = float(input("inserisce la media dei voti: "))

if reddito < 20000 and voti > 27:
    print("La borsa è stata assegnata")
elif reddito >= 20000: 
    print("La borsa è stata rifiutata perchè i redditi sono alti")
elif reddito < 20000 and voti <= 27:
    print("La borsa è stata rifiutata perchè i voti sono bassi")
else: 
    print("La borsa è stata rifiutata")