#Solicita una calificación numérica (0-100) y convierte esa calificación a una letra usando el
#siguiente esquema: A: 90-100,B: 80-89,C: 70-79,D: 60-69,F: 0-59

def calificacionNumerica(nota):
    match  nota:
        case nota if 90 <= nota <= 100:
            return 'A'
        case nota if 80 <= nota <= 89:
            return 'B'
        case nota if 70 <= nota <= 79:
            return 'C'
        case nota if 60 <= nota <= 69:
            return 'D'
        case _:
            return 'F'
nota= int (input("ingrese su calificacion: "))
respuesta= calificacionNumerica(nota)
print ("su calificacion es: ", respuesta)