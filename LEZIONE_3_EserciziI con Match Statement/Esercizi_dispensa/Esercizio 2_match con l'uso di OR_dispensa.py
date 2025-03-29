#ESERCICIO Match Statement and OR/1

# SOLUZIONE CON if/elif/else version)

http_status=200

if http_status==200 or http_status==201:
    print("Success")

elif http_status==400:
    print("Bad request")

elif http_status==404:
    print("Not Found")

elif http_status==500 or http_status==501:
    print("Server Error")

else:
    print("Unknown")

# SOLUZIONE CON MATCH CASE OR 
# or è sostituito con una barra |

http_status=500

match http_status:

    case 200 | 201:
        print("Success")

    case 400:
        print("Bad request")

    case 404:
        print("Not Found")

    case 500 | 501:
        print("Server Error")

    case _:
        print("Unknown")