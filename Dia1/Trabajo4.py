# Solicita al usuario que ingrese las longitudes de los tres lados de un triángulo. 
# Determina si el triángulo es equilátero, isósceles o escaleno

lado1= float (input("ingrese la medida del lado 1: "))
lado2= float (input("ingrese la medida del lado 2: "))
lado3= float (input("ingrese la medida del lado 3: "))

if lado1 == lado2 == lado3:
    print("el triangulo es equilatero")
    
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("el triangulo es isosceles")

else: 
    print ("el triangulo es escaleno")
    