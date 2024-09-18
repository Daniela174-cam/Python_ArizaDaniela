#Escribe un programa que solicite al usuario ingresar su calificacion en un examen y determine si ha aprobado o
# no. Si la calificacion es igual o mayor a 60, muestra el mensaje "Has aprobado". De lo contrario, muestra el mensaje 
#"Has reprobado".

calificacion=float(input("ingrese su nota de examen: "))


aprovado=calificacion>=60
reprovado=calificacion<60
    
if (calificacion>=60):
    print("has aprovado, todavia no sales de campus")
else:
    print("has sido flitrado por el killer")