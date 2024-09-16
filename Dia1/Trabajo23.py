# Escribe un programa que solicite al usuario un número entero positivo n y calcule la suma de los
# primeros n números enteros. Utiliza un ciclo for para realizar la suma.

num = int(input("Ingrese un número entero positivo: "))

if num <= 0:
    print("El número debe ser un entero positivo.")
else:
    suma = 0

    for i in range(1, num + 1):
        suma += i
    print(f"La suma de los primeros {num} números enteros es: {suma}")
