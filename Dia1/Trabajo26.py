# Escribe un programa que solicite al usuario dos números enteros, un valor de inicio y un valor de
# fin. El programa debe imprimir todos los números pares en ese rango, incluyendo los límites. Usa
# un ciclo for para recorrer el rango.

numInicio = int(input("Oe socio, ingrese un número: "))
numFinal = int(input("Parce no me gusto mucho el número, pase otro: "))

if numFinal <= numInicio:
    print("El número final debe ser mayor que el número inicial.")
else:
    for i in range(numInicio, numFinal + 1):
        if i % 2 == 0:
            print(f"El número {i} es par.")
        else:
            print(f"El número {i} es impar.")