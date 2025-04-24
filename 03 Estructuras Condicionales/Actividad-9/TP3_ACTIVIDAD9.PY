magnitud = float(input("Ingrese la magnitud del terremoto (escala de Richter): "))
if magnitud < 4.0:
    print("Muy leve (imperceptible).")
elif magnitud < 4.5:
    print("Leve (poco perceptible).")
elif magnitud < 5.0:
    print("Moderado (sentido por personas, pero generalmente no es dañino).")
elif magnitud < 6.0:
    print("Fuerte (puede causar daños en edificios y estructuras).")
elif magnitud < 7.0:
    print("Muy fuerte (puede causar daños severos en edificios y estructuras).")
else:
    print("Desastroso (puede causar daños catastróficos en áreas pobladas).")   