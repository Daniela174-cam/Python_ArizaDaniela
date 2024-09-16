# Escribe un programa que solicite al usuario ingresar números enteros indefinidamente. El
# programa debe sumar los números siempre que sean pares, pero debe detenerse si el usuario
# ingresa un número impar. Usa un ciclo while para lograr esto.

suma = 0

print("Perro, esto es como su relación, si las cosas son pares sigue, sino, pailas")
print("Si esta vaina no es par, vemos socio")

while True:
    numero = int(input("Suelte un número entero mi compa: "))
    if numero % 2 != 0:
        break
    
    if numero % 2 == 0:
        suma += numero

print(f"la suma de los números enteros es esta mi perro: {suma}, hasta que la cagó porque no sumó más")
