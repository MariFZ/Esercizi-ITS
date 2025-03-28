# 3.8 VEDERE IL MONDO


città: list = ["New York", "Canada", "Mexico", "Cina", "Peru"]

# inserendo la lista dentro le parentesi graffe, stampa la lista dentro la parentesi quadrate.[]:  COSI
# Questo è l'elenco delle città che mi piacerebbe visitare un giorno:['New York', 'Canada', 'Mexico', 'Cina', 'Peru'] 

print(f"Questo è l'elenco delle città che mi piacerebbe visitare un giorno: {città}") 

# con il metodo {', '.join(città)} stampa l'elenco separato di virgole
#print(f"Questo è l'elenco delle città che mi piacerebbe visitare un giorno: {', '.join(città)}")


# Uso di SORTED() NEL PRINT SENZA MODIFICARE LA LISTA. SI DEVE SCRIVERE SORTED DENTRO DEL PRINT
print(f"Stampa della lista in ordine alfabetico, senza modificare l'ordine originale della lista {sorted(città)}")

# PRINT PER DIMOSTRARE CHE ANCORA LA LISTA E' IN DISORDINE
print(f"Stampa della lista nell'ordine originale: {città}")


città.reverse()
print(f"Questo è l'elenco della lista, dove ho inserito citta.reverse all'inizio, che rovescia l'ordine originale: {' , '.join(città)}")

#print(f"Stampa della lista nell'ordine originale: {città}")

città.reverse()
print(f"Questo è l'elenco della lista, dove ho inserito di nuovo 'citta.reverse' all'inizio, e quindi rovescia la lista all'ordine originale com'è stata scritta: {', '.join(città)}")

# USO DI SORT ALL'INIZIO PER MODIFICARE L'ORDINE DELLA LISTA IN ORDINE ALFABETICO

città.sort(reverse=True)
print(f"Elenco della lista con l'uso di sort all'inzio: 'città.sort() e che mette la lista in ordine alfabetico: {', '.join(città)}")

# città.reverse()
# città.reverse()
# print(f"Elenco della lista con l'uso di reverse: 'città.reverse() e che mette la lista in ordine alfabetico alla rovescio: {', '.join(città)}")