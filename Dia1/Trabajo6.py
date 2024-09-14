#El programa genera un número aleatorio entre 1 y 10. El usuario debe adivinar el número, y el
# programa indica si el número ingresado es mayor, menor o igual al número generado.
import random 


adivinanza=(random.randint (1,10))
num = int(input ("ingrese un numero: "))
   

if(num>adivinanza):
    print("el numero es menor")

elif(num<adivinanza):
    print ("el numero es mayor")
    
else:   
    print("has acertado en el blanco")

print ("el numero escondido es: " , adivinanza)