lista = [8, 17, 14, -3, -1, 0]

menor = "inicio"
i = 1

for x in lista:
    if (menor == "inicio"):
        menor = x
    else:
        menor = x if x < menor else menor

print("Numero menor: ", menor)
