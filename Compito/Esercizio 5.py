# Esercizio 5
# Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. 
# Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

# Scrivere un programma che:

# Acquisisca in input un valore N (numero di euro disponibili).
# Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
# Mostri quanti buoni sconto avanzano al termine dell'acquisto.


barretta_free:int = 0
somma_barrette:int = 0
somma_buoni:int = 0
i:int = 0

euro = float(input("Inserisci il denaro: "))

while i < euro: 
        
        somma_barrette += 1
        somma_buoni += 1

        if somma_buoni == 6:
            barretta_free += 1
            somma_buoni -= 6
        i+=1
        
else: 
    print(f"Con i soldi che hai inserito: {int(euro)} euro, puoi acquistare {somma_barrette} barrette, avere {barretta_free} gratuita(e).  I buoni sconto che hai a disposizione sono: {somma_buoni}")