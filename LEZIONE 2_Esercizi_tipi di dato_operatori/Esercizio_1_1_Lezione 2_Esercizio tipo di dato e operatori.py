# ESERCIZIO 1.1 DIMOSTRAZIONE DEL VALORE APROSSIMATIVO DEI NUMERI FLOAT"


x: float = 10.80
y: float = 1.0/10.80


print(f" Valore della variabile Y dopo questa operazione: y: float = 1.0/10.80 è=  {y}") 
print(f" Valore della variabile X è=  {x}") 

prodotto = (x*y)
print(f"Questo è il risultato del prodotto tra X e Y: {prodotto} + che dovrebbe essere 0.9999999")

print(x  -(x*y))
