#Solicita al usuario ingresar el número de materias que ha cursado. Para cada materia, solicita el
# puntaje y determina si ha aprobado o no (>= 60). Luego, calcula el número total de créditos del
#estudiante (cada materia aprobada otorga 3 créditos).

num_materias = int(input("Ingrese la cantidad de materias que ha cursado: "))

materiasAprobadas = 0

for i in range(num_materias):
    puntaje = float(input(f"Ingrese la nota de la materia: {i + 1} "))

    if puntaje >= 60:
        print("La materia se aprobó, un mes mas en campus")
        materiasAprobadas += 1
    else:
        print("Te filtró el killer papi")

creditosTotales = materiasAprobadas * 3

print(f"El total de los creditos es: {creditosTotales}")
