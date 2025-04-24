usuario = input("Ingrese su nombre de usuario: ")
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Usted es un niño")
elif edad >= 12 and edad < 18:
    print("Usted es un adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es un adulto joven")
elif edad > 30:
    print("Usted es un adulto")
    