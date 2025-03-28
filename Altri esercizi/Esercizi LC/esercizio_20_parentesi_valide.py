# esercizio 20 
# Data una stringa scontenente solo i caratteri '(', ')', '{', '}', '['e ']', determina se la stringa di input è valida.

# Una stringa di input è valida se:

# Le parentesi aperte devono essere chiuse con parentesi dello stesso tipo.
# Le parentesi aperte devono essere chiuse nell'ordine corretto.
# Ogni parentesi chiusa ha una parentesi aperta corrispondente dello stesso tipo.

def isvalid(linea:str) ->bool:

    valide:list = []

    coppie:dict[str] = {')':'(', '}':'{', ']':'['}
   
    for segno in linea:
        if segno in coppie.values():
            valide.append(segno)

        elif segno in coppie.keys():
            # if not valide or valide.pop() != coppie[segno]:
            '''un'altra maniera scritta...l'ho separata sotto'''

            if not valide: # controlla se la lista è vuota
                return False # Quindi la stringa non contiene parentesi aperte
            if segno != coppie[segno]: # ci dice quale parentesi aperta corrisponde alla parentesi chiusa attuale# 
                valide.pop() # estrae e rimuove l'ultima parentesi aperta dallo stack
                '''not valide: controlla se la lista è vuota. 
                    Valide.pop() estrae e rimuove l'ultima parentesi aperta dallo stack.
                    coppie[segno] ci dice quale parentesi aperta corrisponde alla parentesi chiusa attuale.
                    Se questi due valori non coincidono, significa che le parentesi non sono abbinate correttamente → la stringa non è valida. '''
               
    
    return len(valide) == 0
            
          

print(isvalid("([])"))   

print(isvalid("()[]{}")) 



            



   

       