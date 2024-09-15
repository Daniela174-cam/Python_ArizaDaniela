#Solicita al usuario que ingrese tres números y determina cuál es el mayor.
num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))
num3=int(input("ingrese el tercer numero: "))

if (num1>num2 and num1>num3):
    print("el primer numero que ingresaste es mayor")
elif(num2>num1 and num2>num3):
    print("el segundo numero que ingresaste es mayor")
else:
    print("el tercer numero que ingresaste es mayor")