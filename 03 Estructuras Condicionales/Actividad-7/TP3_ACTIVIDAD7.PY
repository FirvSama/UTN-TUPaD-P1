string_usuario = input("Por favor, ingresa una frase o palabra: ")

vocales = "aeiouAEIOU"
if string_usuario[-1] in vocales:
    string_resultante = string_usuario + "!"
else:
    string_resultante = string_usuario

print("Resultado:", string_resultante)

