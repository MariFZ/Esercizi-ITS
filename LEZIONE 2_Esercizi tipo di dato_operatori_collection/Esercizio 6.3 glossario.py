# 6.3 Glossario

glossario: dict = {"Items": "Funzione che itera tra le chiavi e il valore, dando i due dati separati ", "Insert": "Richiede 2 argomenti: l'indice dove inserire l'elemento e il nome dell'elemento stesso", "Join": "Usata solo per iterare sulle stringe. Nella sintassi, si deve specificare come separare gli elementi (si devono mettere tra virgolette come si vogliono separare, seguito di .join" , "Funzione Len": "Si scrive prima della variabile per vedere gli elementi", "Metodo Pop": "Rimuove un elemento con questa sintassi: variabile.pop()", "Sorted": "Usato solo nel print per cambiare l'ordine della lista", "Sort": "Usato dopo il nome della lista, per esempio: 'list.sort' e cambia definitivamente l'ordine della lista", "Reverse": "Usato per rovesciare l'ordine della lista", "Upper": "Usato per mettere in maiuscola gli elementi.  Si mette dopo il nome della variabile stringa, così: 'variabile.upper', nel print.  Si può anche usare in una lista usando questa sintassi: {variabile[indice].upper}"}


for parola, significato in glossario.items():
    print(f"\n{parola}: \n{significato}")