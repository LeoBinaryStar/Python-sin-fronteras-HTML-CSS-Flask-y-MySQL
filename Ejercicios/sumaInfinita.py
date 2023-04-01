lista = []
print('Ingrese números y para salir escriba "basta"')
while True:
    valor = input('Ingrese valor: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = float(valor)
            lista.append(valor)
        except:
            print('Dato inválido')
            exit()
resultado = 0
for x in lista:
    resultado += x

print("El resultado de todos los numeros ingresados es: ", resultado)
