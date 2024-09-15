#El programa contiene una letra secreta (por ejemplo, "A"). El usuario debe adivinar la letra, y el
#programa le indicará si acertó o no.

import random 
import string

letras = string.ascii_uppercase
adivinanza=(random.choice (letras))
letra= input ("ingrese una letra : ").upper()

if(letra!=adivinanza):
    print("la letra es incorrecta")

else:   
    print("has acertado en el blanco")
    
print ("la letra escondido es: " , adivinanza)
