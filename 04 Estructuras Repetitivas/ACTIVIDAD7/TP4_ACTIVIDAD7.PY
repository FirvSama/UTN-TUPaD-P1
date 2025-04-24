numero = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(0, numero + 1):
    suma += i

print(f"La suma de los numeros desde 0 hasta", numero, "es:", suma)
