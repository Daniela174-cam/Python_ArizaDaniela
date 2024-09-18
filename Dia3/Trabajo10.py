#Crea un programa que solicite al usuario ingresar una serie de numeros positivos y luego calcule e imprima el promedio de los
#numeros ingresados utilizando un bucle while. El programa debe terminar cuando el usuario ingrese un numero negativo.

# Programa para calcular el promedio de números positivos
total = 0
contador = 0

while True:
    numero = float(input("Ingresa un número positivo (o un número negativo para terminar): "))
    
    if numero < 0:
        break  # Termina el bucle si el número es negativo
    
    total += numero
    contador += 1

if contador > 0:
    promedio = total / contador
    print(f"El promedio de los números ingresados es: {promedio:.2f}")
else:
    print("No ingresaste ningún número positivo.")
