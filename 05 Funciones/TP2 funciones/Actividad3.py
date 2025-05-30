def informacion_personal(nombre, apellido, edad , residencia):
    print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}, Residencia: {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)