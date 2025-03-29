# ESERCIZIO 3C-6 
# Modificare l'esercizio 3C-4, che consenta all'utente di inserire il nome di un animale ed un habitat. 

# Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, 
# oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. 
# Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".


mammiferi: list[str] = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili: list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli: list[str] = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci: list[str] = ["squalo", "trota", "salmone", "carpa"]
unknow: list[str] = []

animal_type: dict[str] = {}

nome_animale: str = (input("Inserisci il nome di un animale che per identificare a quale categoria appartiene: "))
habitat_animale: str = (input(f"Digita l'habitat in cui vive l'animale: \"{nome_animale}\" (acqua/aria/terra): "))


match nome_animale, habitat_animale:

    # mammiferi nell'acqua: balena, delfino
    case nome_animale if nome_animale in mammiferi:
        animal_type[nome_animale] = "mammiferi"
    
    case habitat_animale if habitat_animale == "acqua": 
        animal_type[habitat_animale] = "acqua"

    # mammiferi nella terra: cane, gatto
    case habitat_animale if habitat_animale == "terra": 
        animal_type[habitat_animale] = "terra"
    
        print(f"L'animale che hai scritto: \"{nome_animale}\" appartiene alla categoria dei Mammiferi!")

    # rettili nell'acqua: coccodrillo
    case nome_animale if nome_animale in rettili:
        animal_type[nome_animale] = "rettili"

    case habitat_animale if habitat_animale == "acqua": 
        animal_type[habitat_animale] = "acqua"
    
    # rettili nella terra: serpente

    case habitat_animale if habitat_animale == "terra": 
        animal_type[habitat_animale] = "terra"
      

        print(f"L'animale che hai scritto: \"{nome_animale}\" appartiene alla categoria dei rettili!")

    # ucceli nell'acqua: anatra

    case nome_animale if nome_animale in uccelli:
        animal_type[nome_animale] = "uccelli"


    case habitat_animale if habitat_animale == "acqua": 
        animal_type[habitat_animale] = "acqua"


    # uccelli nella aria: aquila
    case habitat_animale if habitat_animale == "aria": 
        animal_type[habitat_animale] = "aria"
        

        print(f"L'animale che hai scritto: \"{nome_animale}\" appartiene alla categoria degli Uccelli!")

    # pesci nell'acqua
    case nome_animale if nome_animale in pesci:
        animal_type[nome_animale] = "pesci"
        print(f"L'animale che hai scritto: \"{nome_animale}\" appartiene alla categoria degli pesci!")

    case _:
        animal_type[nome_animale] = "unknow"
        print(f"L'animale: \"{nome_animale}\" è stato inserito alla categoria 'Sconosciuta'")


print(f"Questi sono gli animali che sono nella variabili: tipo di animali {animal_type}")


tipo_animale: dict = {"nome": nome_animale, "habitat": animal_type[habitat_animale], "categoria": animal_type[nome_animale]}
# tipo_animale: dict = {"nome": nome_animale, "habitat": habitat_animale, "categoria": animal_type[nome_animale]}


print(f"Tipo animale {tipo_animale}")


match tipo_animale:
   
    # mammiferi


    # case {"nome": name, "habitat": "terra", "categoria": "mammiferi"} if {"habitat" ["terra": "acqua"]}: 

    case {"nome": name, "habitat": "terra", "categoria": "mammiferi"}:       # name qui è una variabile volatile che mi prende il valore della chiave di nome
        print(f"L'animale {name} appartiene alla categoria dei MAMMIFERI che vivono nella terra!")
        print(f"L'animale {name} può vivere l'habitat {habitat_animale}")
    
 

    case {"nome": name, "habitat": "acqua", "categoria": "mammiferi"}:       # name qui è una variabile volatile che mi prende il valore della chiave di nome
        print(f"L'animale {name} appartiene alla categoria dei MAMMIFERI che vivono nell'acqua!")
        print(f"L'animale {name} può vivere l'habitat {habitat_animale}")

    # ECCESSIONE




    # RETTILI CHE VIVONO NELL'ACQUA

    case {"nome": name, "habitat": "acqua", "categoria": "rettili"}:       # name qui è una variabile volatile che mi prende il valore della chiave di nome
        print(f"L'animale {name} appartiene alla categoria dei RETTILI che vivono nell'acqua!")
        print(f"L'animale {name} può vivere l'habitat {habitat_animale}")

    # RETTILI CHE VIVONO NELLA TERRA

    case {"nome": name, "habitat": "terra", "categoria": "rettili"}:       # name qui è una variabile volatile che mi prende il valore della chiave di nome
        print(f"L'animale {name} appartiene alla categoria dei RETTILI che vivono nella terra!")
        print(f"L'animale {name} può vivere l'habitat {habitat_animale}")

    
    # UCCELLI CHE VIVONO NELL'ACQUA

     
    case {"nome": name, "habitat": "acqua", "categoria": "uccelli" }:       # name qui è una variabile volatile che mi prende il valore della chiave di nome
        print(f"L'animale {name} appartiene alla categoria dei UCCELLI! che vivono nell'acqua")
        print(f"L'animale {name} può vivere l'habitat {habitat_animale}")


    # UCCELLI CHE VIVONO NELL'ARIA

    case {"nome": name, "habitat": "aria", "categoria": "uccelli"}:      # name qui è una variabile volatile che mi prende il valore della chiave di nome
        print(f"L'animale {name} appartiene alla categoria UCCELLI! che vivono nell'aria!")
        print(f"L'animale {name} può vivere l'habitat {habitat_animale}")

    
    # case {"nome": name, "habitat": ambiente, "categoria": "unknow"}:      # name qui è una variabile volatile che mi prende il valore della chiave di nome
    #     print(f"L'animale {name} appartiene alla categoria dei pesci!")
    #     print(f"L'animale {name} può vivere sull'acqua!")


    case {"nome": name, "categoria": "unknow"}:      # name qui è una variabile volatile che mi prende il valore della chiave di nome
        print(f"Non so dire in quale categoria classificare l'animale {name}")
        print(f"Non sono in grado di fornire informazioni sull'habitat!")


    case _:
        print(f"Non so dire in quale categoria classificare l'animale:  {nome_animale}")
        print(f"Non sono in grado di fornire informazioni sull'habitat")










