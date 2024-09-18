#Escribe un programa que solicite al usuario ingresar el dia, el mes y el año de
#una fecha. Luego, verifica si la fecha es valida o no. Considera los diferentes
#casos, como los dias de cada mes y si el año es bisiesto. Muestra un mensaje
#indicando si la fecha es valida o no.

import calendar

# Función para verificar si el año es bisiesto
def es_bisiesto(anio):
    return calendar.isleap(anio)

# Función para verificar si la fecha es válida
def es_fecha_valida(dia, mes, anio):
    # Verificar si el mes está en el rango correcto (1-12)
    if mes < 1 or mes > 12:
        return False
    
    # Verificar si el día está en el rango correcto para el mes y año dados
    if dia < 1 or dia > calendar.monthrange(anio, mes)[1]:
        return False
    
    return True

# Solicitar al usuario que ingrese el día, mes y año
dia = int(input("Ingresa el día (1-31): "))
mes = int(input("Ingresa el mes (1-12): "))
anio = int(input("Ingresa el año: "))

# Verificar si la fecha es válida
if es_fecha_valida(dia, mes, anio):
    print(f"La fecha {dia}/{mes}/{anio} es válida.")
else:
    print(f"La fecha {dia}/{mes}/{anio} es inválida.")
