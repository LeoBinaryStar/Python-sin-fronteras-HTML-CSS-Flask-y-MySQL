def ParImpar(numero):
    residuo = numero % 2
    if residuo == 0:
        print("Es par")
    else:
        print("Es impar")


numero = float(input("Ingrese su numero: "))
ParImpar(numero)
