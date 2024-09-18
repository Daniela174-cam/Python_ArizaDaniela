#Escribe un programa que solicite al usuario ingresar su calificacion en un examen y determine si ha aprobado o
# no. Si la calificacion es igual o mayor a 60, muestra el mensaje "Has aprobado". De lo contrario, muestra el mensaje 
#"Has reprobado".

nota=float(input("ingrese la nota de su calificacion: "))

def notas(calificacion):
    if nota>=60:
        print("has aprobado, felicitaciones")
        else:
            print("te va a filtar Johlver ")