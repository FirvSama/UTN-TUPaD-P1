
# 1) Agregar frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("1) Diccionario actualizado:", precios_frutas)

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("2) Precios actualizados:", precios_frutas)

# 3) Lista de frutas (sin precios)
lista_frutas = list(precios_frutas.keys())
print("3) Lista de frutas:", lista_frutas)

# 4) Agenda telefónica
agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingrese el nombre del contacto a consultar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# 5) Solicitar 10 números y guardarlos en una tupla
numeros = []
for i in range(10):
    n = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(n)
tupla_numeros = tuple(numeros)
print("5) Tupla de números:", tupla_numeros)

# 6) Mostrar el mayor y menor valor de la tupla
print("6) Mayor:", max(tupla_numeros), "Menor:", min(tupla_numeros))

# 7) Crear un conjunto con los valores únicos de la tupla
conjunto_unicos = set(tupla_numeros)
print("7) Conjunto de valores únicos:", conjunto_unicos)

# 8) Crear un diccionario con los números de la tupla y su cuadrado
diccionario_cuadrados = {n: n**2 for n in tupla_numeros}
print("8) Diccionario de cuadrados:", diccionario_cuadrados)

# 9) Contar cuántas veces aparece cada número en la tupla
conteo = {}
for n in tupla_numeros:
    conteo[n] = conteo.get(n, 0) + 1
print("9) Frecuencia de cada número:", conteo)

# 10) Mostrar los números que aparecen más de una vez
repetidos = [n for n, c in conteo.items() if c > 1]
print("10) Números repetidos:", repetidos)
