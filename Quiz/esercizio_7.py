# esercizio 7

# Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
# cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
# For example

# print(check_parentheses("()()"))
# True
# print(check_parentheses("(()))("))
# False


def check_parentheses(expression: str) -> bool:
   '''Funzione che verifica se una stringa contiene parentesi bilanciate.
   Restituisce True se ogni '(' ha un ')' corrispondente e nell'ordine corretto, altrimenti False.

   La expression: str è la stringa che contiene le parentesi da controllare
   bool: True se le parentesi sono bilanciate, sino False '''
   
   # creo una lista che conterrà le parentesi aperte
   bilanciato:list[str] = []
    
   # itero su ogni carattere della stringa
   for segno in expression:
        if segno == "(":
            '''Se il carattere è una parentesi aperta '(' lo aggiungiamo alla lista'''
            bilanciato.append(segno)  # Aggiungiamo un'apertura alla lista

        elif segno == ")":
            # Se il carattere è una parentesi chiusa ')'
            if not bilanciato:  
                '''verifichiamo che la lista non sia vuota, non ci sono parentesi aperte'''
                return False # Quindi la stringa non contiene parentesi aperte
            
            '''Se la lista non è vuota, rimuoviamo l'ultima parentesi aperta'''
            bilanciato.pop()  

   return len(bilanciato) == 0  # Se lo stack è vuoto, le parentesi sono bilanciate

# print(check_parentheses("()()"))

# print(check_parentheses("(()))("))

# print(check_parentheses("((()))"))

# print(check_parentheses(")("))

# print(check_parentheses("(())"))


# # Spiegazione col primo esempio: ("()()"))

# def check_parentheses(expression: str) -> bool:
#    '''esempio: 
#       ("()()"))
      
#       '''
   
#    bilanciato:list[str] = [] # Creo una lista vuota
   
'''Analizziamo la stringa, carattere per carattere:
   
   * Primo carattere: '(' :   è una parentesi aperta, l'aggiungo alla lista:

   bilanciato.append(segno)
   bilanciato = ['('] # appare così

   * Secondo carattere: '(':  è una parentesi aperta, l'aggiungo alla lista:
   
   bilanciato.append(segno)

   bilanciato = ['(', '(] # appare cosi

   * Terzo carattere: ')':  è una parentesi chiusa, eliminiamo l'ultimo elemento aggiunto: una parentesi aperta: '('

   Come si fa? Si usa .pop() che elimina l'ultimo elemento della lista, senza bisogno di specificare qual è:
   
   bilanciato.pop()     # Rimuove l'ultima '('

   bilanciato = ['(']   # Rimane solo una '(' nello stack

   * Quarto carattere: ')' : è una parentesi chiusa

   rimuovo una parentesi aperta
   
   bilanciato.pop()  # Rimuove l'ultima '('
   bilanciato = []  # Lo stack ora è vuoto

   Se la lista è vuota, restituimo True, le parentesi sono bilanciate


   '''


# uso del metodo append e pop

# stack = []

# stack.append("A")  # Aggiunge "A" alla fine
# print(stack)
# stack.append("B")  # Aggiunge "B" alla fine
# print(stack)
# stack.append("C")  # Aggiunge "C" alla fine
# print(f"{stack}\n")

# # print(stack)  # Output: ['A', 'B', 'C']

# last_element = stack.pop()  # Rimuove l'ultimo elemento aggiunto ("C")
# print(last_element)  # Output: C
# last_element = stack.pop() # Output B
# print(last_element)  # toglo
# last_element = stack.pop()
# print(stack)  # Output: ['A', 'B']

# Uso di not
'''Per verificare se una lista/dizionario è vuoto, 
   basta scrivere not dopo il nome della collection

   per esempio:

   if not lista
   if not dizionario
   if not set



bilanciato = []  # Lista vuota

# Verifica se la lista è vuota
if not bilanciato:
    print("La lista è vuota!")  # Questo verrà stampato
else:
    print("La lista NON è vuota.")'
'''


      


