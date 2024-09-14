#Solicita al usuario que ingrese un número y determina si es positivo, negativo o cero.

num=float(input("ingrese numero: "))
if (num<0):
    print("el numero ingresado es negativo")
elif(num>0):
    print("el numero ingresado es positivo")
else:
    print("el numero ingresado es cero")

