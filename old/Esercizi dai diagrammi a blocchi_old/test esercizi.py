# ESERCIZIO 2 - DIAGRAMMA A BLOCCHI SECONDA PARTE

# Automazione di un semaforo intelligente
'''Progettare un algoritmo che simuli il comportamento di un semaforo intelligente. Questo sistema deve adattare i tempi di durata (espressi in percentuale) del verde in base al numero di veicoli presenti sulle principali direzioni di traffico: Nord-Sud ed Est-Ovest. Ogni direzione può ricevere una priorità se il numero di veicoli supera una soglia predefinita.

Requisiti:

Se il numero di veicoli in una sola direzione supera la soglia (es. 70 veicoli), quella direzione riceve un tempo minimo garantito per il verde (es. 60%) e il restante tempo è assegnato all'altra direzione.
Se entrambe le direzioni superano la soglia, il tempo è equamente suddiviso (50% per ciascuna direzione).
Se nessuna direzione supera la soglia, il tempo è calcolato proporzionalmente al numero totale di veicoli nelle due direzioni.
Stampare la percentuale del tempo assegnato al verde per ciascuna direzione.'''

num_NS = input("")
num_EO = input("")

soglia = int(input("Inserisci la soglia"))
tempo_priorita = int(input("Inserisci il tempo di priorita"))

if num_NS > soglia:

    if num_EO > soglia:
        tempo_NS = 50
        tempo_EO = 50
    else:
        tempo_NS = tempo_priorita
        tempo_EO = 100 - tempo_priorita

elif num_EO > soglia:
    
    tempo_NS = 100 - tempo_priorita
    tempo_EO = tempo_priorita
    
else: 
    veicoli_tot = num_NS + num_EO
    tempo_NS = num_NS/veicoli_tot * 100
    tempo_EO = 100 - tempo_NS

print("Risultato: {tempo_EO} e {tempo_NS}") 






