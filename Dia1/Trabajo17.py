#Solicita la calificación del estudiante y pregunta si hizo tareas adicionales. Si la respuesta es "sí",
# añade un 5% extra a la calificación, pero si la calificación supera 100, ajústala a 100. Si la respuesta
# es "no", simplemente muestra la calificación original.

def notaEstudiante(nota, respuesta):
    match str (respuesta):
        case "sikas":
            return nota + 5
        case "nokas":
            return nota
        case _:
            return "respuesta invalida"

nota = float(input("cual es su nota perro?: "))
respuesta = input("este año le lambio también o no? (sikas o nokas perro): ")
resultado = notaEstudiante(nota, respuesta)
notaMaxima = 100
if nota>= notaMaxima:
    print("su nota final fue: ", notaMaxima)
else:
    print("su nota final fue: ", resultado)