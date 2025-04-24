nombre = input("Ingrese su nombre: ") 
print("Seleccione una opcion: ")
print("1. nombre en MAYUSCULAS")
print("2. nombre en minusculas")
print("3. nombre con Primer Letra en Mayuscula")

opcion = input("Ingrese el numero de la opcion (1, 2 o 3): ")
if opcion == "1":
    print("Resultado: ", nombre.upper())
elif opcion == "2":
    print("Resultado: ", nombre.lower())    
elif opcion == "3": 
    print("Resultado: ", nombre.title())
else:   
    print("Opcion no valida, Por favor, ingrese 1, 2 o 3")
    
