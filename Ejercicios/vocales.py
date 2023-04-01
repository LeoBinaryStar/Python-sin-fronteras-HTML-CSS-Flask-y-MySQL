print("Ingrese su palabra:")
palabra = str(input(""))
numVocales = 0


for x in palabra:
    z = x.lower()  # Toda la cadena a minusculas e igual el metodo upper() puede funcionar en caso de mayusculas
    if (z == "a" or z == "e" or z == "i" or z == "o" or z == "u"):
        numVocales += 1
    else:
        numVocales += 0
print("Su numero de vocales es: ", numVocales)
