number: int = input("Inserisce un numero: ")

match number:
    case 1:
        print(f"Questo è il numero cardinale {number}st!")

    case 2:
        print(f"Questo è il numero cardinale {number}nd!")

    case 3:
         print(f"Questo è il numero cardinale {number}rd!")

    case _:
        print(f"Questo è il numero cardinale {number}th!")