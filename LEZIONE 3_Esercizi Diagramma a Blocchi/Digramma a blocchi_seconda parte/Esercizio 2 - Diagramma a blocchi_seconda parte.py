# ESERCIZIO 2. Automazione di un semaforo intelligente

# Progettare un algoritmo che simuli il comportamento di un semaforo intelligente. Questo sistema deve adattare i tempi di durata (espressi in percentuale) del verde 
# in base al numero di veicoli presenti sulle principali direzioni di traffico: Nord-Sud ed Est-Ovest. 
# Ogni direzione può ricevere una priorità se il numero di veicoli supera una soglia predefinita.

'''Requisiti:

Se il numero di veicoli in una sola direzione supera la soglia (es. 70 veicoli), quella direzione riceve un tempo minimo garantito per il verde (es. 60%) e il restante tempo è assegnato all'altra direzione.
Se entrambe le direzioni superano la soglia, il tempo è equamente suddiviso (50% per ciascuna direzione).
Se nessuna direzione supera la soglia, il tempo è calcolato proporzionalmente al numero totale di veicoli nelle due direzioni.'''


vei_ns = int(input("Inserisci il numero di veicoli nella direzione Nord-Sud: "))

vei_eo = int(input("Inserisci il numero di veicoli nella direzione Est-Ovest: "))

soglia = int(input("Inserisci la soglia di veicoli in fila: "))

tempo_garantito = int(input("Inserisce il tempo di priorità: "))

if vei_ns > soglia and vei_eo > soglia:
    # Se entrambe le direzioni superano la soglia, il tempo viene diviso equamente
        tempo_ns = 50
        tempo_eo = 50
    
elif vei_ns > soglia:
    # Se solo la direzione Nord-Sud supera la soglia
    tempo_ns = tempo_garantito
    tempo_eo = 100 - tempo_garantito

elif vei_eo > soglia:
    # Se solo la direzione Est-Ovest supera la soglia
    tempo_eo = tempo_garantito
    tempo_ns = 100 - tempo_garantito

else:
    # Se nessuna direzione supera la soglia, si assegna il tempo proporzionalmente
    totale_veicoli = (vei_eo + vei_ns)
    tempo_ns = ((vei_ns / totale_veicoli) * 100)
    tempo_eo = ((vei_eo / totale_veicoli) * 100)
   
# Stampo il risultato, nel primo scrivo con solo 2 cifre dopo la virgola, nel secondo con tutti numeri dopo
print(f"Il tempo per i veicoli nella direzione Nord-Sud sarebbe: {tempo_ns:.2f}% e il tempo per Est-Ovest sarebbe: {tempo_eo}%")


