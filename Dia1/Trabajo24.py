# Escribe un programa que solicite al usuario una cadena de texto y cuente cuántas vocales (a, e, i,
# o, u) contiene. Usa un ciclo for para recorrer la cadena y realizar la cuenta.

texto = input("Ingrese una cadena de texto: ")

contador_vocales = 0

vocales = "aeiou"

for i in texto:
    if i.lower() in vocales:
        contador_vocales += 1

print(f"La cantidad de vocales en el texto es: {contador_vocales}")
