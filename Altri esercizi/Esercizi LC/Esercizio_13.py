# Esercizio 13
# Da romano a intero

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Ad esempio,  2 è scritto come II in numeri romani, solo due unità sommate. 12 è scritto come  XII, che è semplicemente X + II. Il numero 27 è scritto come XXVII, 
# che è XX + V + II.

# I numeri romani sono solitamente scritti dal più grande al più piccolo da sinistra a destra. 
# Tuttavia, il numero per quattro non è IIII. Invece, il numero quattro è scritto come IV. Poiché l'uno è prima del cinque, 
# lo sottraiamo ottenendo quattro. Lo stesso principio si applica al numero nove, che è scritto come IX. 

 

# Ci sono sei casi in cui viene utilizzata la sottrazione:

# I può essere posizionato prima di V(5) e X(10) per formare 4 e 9. 
# X può essere posizionato prima di L(50) e C(100) per formare 40 e 90. 
# C può essere posizionato prima di D(500) e M(1000) per ottenere 400 e 900.
# Dato un numero romano, convertilo in un numero intero.



# numbers: list[int] = list(range(1, 1001))

numbers = range(1, 1001)
# print(numbers)  
# Output: range(1, 1001)  → Non è una lista, ma un oggetto iterabile

match numbers:
    case < 4:
        






