cantidad_numeros = 100
suma = 0

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

media = suma / cantidad_numeros

print(f"La media de los numeros ingresados es:", media)
