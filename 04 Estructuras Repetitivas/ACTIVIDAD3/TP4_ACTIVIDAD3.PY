inicio = int(input("Ingrese el primer numero: "))
fin = int(input("Ingrese el segundo numero: "))

if inicio > fin:
    inicio, fin = fin, inicio
suma = 0
for i in range(inicio, fin + 1):
    suma += i
print("La suma de los numeros entre", inicio, "y", fin, "es:", suma)    