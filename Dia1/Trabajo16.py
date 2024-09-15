#Solicita al usuario la distancia a recorrer (en km) y la velocidad promedio del automóvil (en km/h).
# Calcula el tiempo de viaje en horas y minutos. Si la velocidad es mayor a 120 km/h, muestra un
# mensaje de advertencia.

def calcular_velocidad(distancia,velocidad):
    
    formula_DistanciaHoras = distancia/velocidad

    if (velocidad>120):
        print("cuidado ahi rayo macqueen!!")
    return formula_DistanciaHoras

distancia=float(input("ingrese su distancia a recorrer: "))
velocidad=float(input("ingrese la velociadad promedio de su automovil: "))
resultadoHoras = calcular_velocidad(distancia, velocidad)
formula_DistanciaMinutos =  resultadoHoras*60
print("Su recorrido en horas es: ", resultadoHoras)
print("Su recorrido en minutos es de: ", formula_DistanciaMinutos)