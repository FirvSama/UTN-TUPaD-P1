usuario = input("Ingrese su nombre: ")
Nota = int(input("Ingrese su nota: "))
if Nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    print("Vuelva a intentarlo")
    print("Hasta luego", usuario)