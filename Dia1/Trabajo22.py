# Escribe un programa que clasifique un triángulo en agudo, obtuso o rectángulo según sus ángulos
# internos usando if .
# Solicita al usuario los tres ángulos de un triángulo y clasifícalo en:
# Agudo: Todos los ángulos son menores a 90°.
# Rectángulo: Un ángulo es exactamente 90°.
# Obtuso: Un ángulo es mayor a 90°.
Lado1 = float(input("Ingrese Angulo de lado 1: "))
Lado2 = float(input("Ingrese Angulo de lado 2: "))
Lado3 = float(input("Ingrese Angulo de lado 3: "))

if Lado1 + Lado2 + Lado3 != 180:
    print("Los ángulos ingresados no forman un triángulo válido.")
else: 
    if Lado1 < 90 and Lado2 < 90 and Lado3 < 90:
        print("Su triángulo es un triángulo agudo.")
    elif Lado1 == 90 or Lado2 == 90 or Lado3 == 90:
        print("Su triángulo es un triángulo rectángulo.")
    else:
        print("Su triángulo es un triángulo obtuso.")