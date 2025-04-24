usuario = input("Por favor Ingrese su Nombre de Usuario: ")
Edad = int(input("Por favor Ingrese su Edad: "))
if Edad >= 18: 
    print("Bienvenido", usuario, "usted es mayor de edad")
else: 
    print("Lo siento", usuario, "usted es menor de edad")
    print("No puede ingresar al sistema")
    print("Hasta luego", usuario)
