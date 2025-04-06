# Ripaso 03 aprile

# Inversione di una stringa
# Scrivere una funzione inversione_stringa(testo) che, ricevuta come argomento una stringa, restituisca la sua inversione. 
# Potete assumere che l’argomento sia sempre una stringa.

# def inversione_stringa(s:str) -> str:
#     stringa_invertita = s[::-1]

#     return stringa_invertita

# # stringa_1: str = "Maritza"

# print(inversione_stringa("Maria"))

# Esercizio 2
# Numeri compresi in intervallo
# Scrivere una funzione compresi(L,low,high) che restituisca il numero di valori nella lista L che sono compresi tra low e high (estremi compresi).
# Potete assumere che gli argomenti siano di tipo corretto e che la lista contenga solo valori numerici.

# def compresi(L:list, low:int, high:int) ->int:

#     lista_compressa:list = []

#     for elemento in L:
#         if elemento <= high and elemento >=low:
#             lista_compressa.append(elemento) 

#     return len(lista_compressa)

# seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4] 
# n = compresi(seq,3,5) 
# print(n)


# Verifica di ordinamento (5 punti)
# Scrivere una funzione ordinata(L) che data una lista L come argomento, verifichi che L sia ordinata in modo crescente. 
# Potete assumere che L sia costituita da tutti elementi confrontabili e che quindi la nozione di ordinamento abbia senso. 
# Se L è ordinata in modo crescente allora la funzione deve restituire True, e deve restituire False in caso contrario.


# def ordinata(l:list) -> bool:
    
#     return l == sorted(l)

    
# seq1 = [3,5,1,8,4,2,5,7] 
# seq2 = ["delfino", "gatto", "renna", "tacchino"]


# print(ordinata(seq1))
# print(ordinata(seq2))

# 4 Bordo della Matrice (4 punti)
# Scrivere una funzione bordo_zero(M) che prenda come argomento una matrice rettangolare di dimensioni 𝑟 × 𝑐 con 𝑟 ≥ 1 e 𝑐 ≥ 1, 
# che restituisca True se il bordo della matrice è costituito esclusivamente da zeri, e che restituisca False altrimenti. 
# Potete assumere che M sia una lista di liste, tutte contenenti numeri, e della stessa lunghezza. Potete assumere che la
# matrice, così rappresentata, abbia almeno una riga e una colonna.

def bordo_zero(m:list) ->bool:
    
    return m[0]  == 0 or m[-1] == 0

M1 = [[0]]
M2 = [[0,0,0,0], [0,7,8,0] , [0,0,0,0]]
print(bordo_zero(M1))
print(bordo_zero(M2))

# risposta corretta

def bordo_zero(m: list) -> bool:
    righe, colonne = len(m), len(m[0])

    # Estraggo tutti gli elementi del bordo in un'unica lista
    bordo = (
        m[0] +  # Prima riga
        m[-1] +  # Ultima riga
        [m[i][0] for i in range(1, righe - 1)] +  # Prima colonna (escludendo angoli)
        [m[i][-1] for i in range(1, righe - 1)]  # Ultima colonna (escludendo angoli)
    )

    return all(x == 0 for x in bordo)  # Verifica se tutto il bordo è zero







