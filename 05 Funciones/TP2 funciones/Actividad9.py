def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius:.2f}ºC equivalen a {fahrenheit:.2f}ºF")