numero = int(input("Ingrese un numero entero: "))
contador_digitos = 0
if numero == 0:
    contador_digitos = 1
else:
    while numero > 0:
        numero //= 10
        contador_digitos += 1
print("El numero tiene", contador_digitos, "digitos")
    