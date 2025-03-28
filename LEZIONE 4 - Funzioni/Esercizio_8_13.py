# ESERCIZIO 8.13
# User Profile

# Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. 
# All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67

# Costruite un profilo di voi stessi chiamando build_profile(), utilizzando il vostro nome e cognome e altre tre coppie chiave-valore che vi descrive. 
# Ogni parametro deve essere passati alla funzione come parametri. La funzione deve restituire una stringa come "Eric Crow, età 45 anni, capelli castani, peso 67".

def build_profile(nome, cognome, **myself): 

    iosono: dict = {'mio_nome': nome, 'mio_cognome': cognome}

    for chiave, valore, in myself.items():
        iosono[chiave] = valore

    return iosono


amalia = build_profile("Amalia", "Palacio", eta= 3, altezza= 58, capelli= "marroni")

print(amalia)




























































# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
    
    
# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

# # my_profile = build_profile('James', 'Bond', location = 'London', field = 'Math')

# print(user_profile)
# # print(my_profile)