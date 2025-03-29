# Esercizio 11 - Quiz
'''Esercizio non avuto'''

# Scrivi una funzione chiamata convert_temperature che prenda due parametri:
# temperature: il valore numerico della temperatura, 
# to_celsius (opzionale): un valore booleano che indica se la temperatura deve essere convertita in Celsius. 
# Se to_celsius è True, la funzione deve convertire da Fahrenheit a Celsius; se to_celsius è False o non viene fornito, 
# la funzione deve convertire da Celsius a Fahrenheit.

from typing import Optional

def convert_temperature(temperature:float, to_celsius: Optional[bool] = None) ->float:

    
    if to_celsius: 
        '''Quando si scrive: if to...., Python l'interpreta come True'''
        # converte da Fahrenheit a Celsius
        return (temperature -32) * 5/9
    
    elif not to_celsius:
        return (temperature* 9/5) +32
    
    else:
        return (fahrenheit, to_celsius)

fahrenheit = 100
celsius = 37.5

print(f"Questo è il valore di F: {convert_temperature(fahrenheit):.2f}")
      

print(f"Questo è il valore di C: {convert_temperature(celsius):.2f}")
print(f"Questo è il valore di tutte e due: 'Fare'{convert_temperature(fahrenheit):.2f} e Cels: {convert_temperature(celsius)}")


# # seconda possibilità partendo da to_celsius come

# def convert_temperature(temperatura:float, to_celsius: Optional[bool] = None) -> float:

#     fahrenheit:float = 0,0
#     celsius:float = 0,0

#     if to_celsius is None or not to_celsius:
#         # converte da celsius a Fahrenheit

#         fahrenheit:float = (temperatura* 9/5) +32

#     else:
#         celsius:float = (temperatura -32) * 5/9

#     return fahrenheit, celsius


# fahrenheit = 100
# # celsius = 37.5
# print(convert_temperature(fahrenheit))








# Esercizio 2469 - Converti la temperatura

# Ti viene fornito un numero in virgola mobile non negativo, arrotondato a due cifre decimali celsius, che indica la temperatura in gradi Celsius .
# Dovresti convertire Celsius in Kelvin e Fahrenheit e restituirlo come un array ans = [kelvin, fahrenheit].
# Restituisce l'array ans. Saranno accettate le risposte che rientrano nella risposta effettiva.10-5

# Notare che:
# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00

# def convert_in_Kelvin_Fah(celsius:float = 0.00) ->list:

#     temperature:list[float] = []

#     #to Celsius a Kelvin
#     kelvin:float = celsius + 273.15
#     temperature.append(kelvin)

#     # to Celsius to Fahrenheit = 
#     fahrenheit:float = (celsius * 1.80) + 32.00
#     temperature.append(fahrenheit)

#     return temperature

# celsius_value = 36.50
# print(convert_in_Kelvin_Fah(celsius_value)) # di questa maniera, mi stampa solo i valori separati da virgola

# result= convert_in_Kelvin_Fah(celsius_value) # result sarà una lista con Kelvin e Fahrenheit
# print(f"{celsius_value}°C = {result[0]:.2f}K, {result[1]:.2f}°F")







