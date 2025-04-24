import random
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    
    if intento == numero_secreto:
        adivinado = True


print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")   