# Escribe un programa que solicite al usuario un número entero positivo n y calcule el factorial de
# dicho número ( n! = 1 * 2 * 3 * ... * n ). Usa un ciclo for para realizar el cálculo.

num = int(input("Ingrese un número entero positivo: "))

factorial = 1

if num < 0:
    print("El número debe ser un entero positivo.")
else:
    for i in range(1, num + 1):
        factorial *= i

    print(f"El factorial de {num} es: {factorial}")
