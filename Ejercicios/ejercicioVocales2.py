palabra = 'ChanchitoFeliz'
vocales = 0
lista = ['a', 'e', 'i', 'o', 'u']
for x in palabra:
    for y in lista:
        vocales += 1 if x.lower() == y else 0
print(vocales)
