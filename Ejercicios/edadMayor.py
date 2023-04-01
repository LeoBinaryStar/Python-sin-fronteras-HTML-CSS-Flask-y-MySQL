def esMayor():
    if edad >= 18:
        Mayor = True
        print("Ustede es mayor...", Mayor)
    else:
        Mayor = False
        print("Ustede es mayor...", Mayor)


edad = float(input("Ingrese su edad: "))
esMayor()
