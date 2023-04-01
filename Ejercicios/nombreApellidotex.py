def Registrar(nombre, apellido):
    c = open("registro.txt", "a")
    c.write(nombre + "\n" + apellido)
    c.close


nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
Registrar(nombre, apellido)
