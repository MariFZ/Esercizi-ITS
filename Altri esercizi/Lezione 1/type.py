string1 = "Hello World"


# multi-line string 
string2 = "This is \
a string \
too "

# string leght 
print(len(string1))

# display string first char
print(string1[0])

print(string1[6])

print(string1[10])

'''# ATTENZIONE: questa stringa * print(string1[11] *  da errore 
perchè sta richiendo più caratteri di quelli che ha la parola Hello World (ha 10 lettere)'''

# Lowercase - tutta con lettere minuscole
print(string1.lower())

# Uppercase - tutte le i caratteri maiuscoli
print(string1.upper())

# Title case 
print(string1.title())

