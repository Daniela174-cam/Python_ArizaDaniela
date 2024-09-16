# El instituto nacional de sismologia desea una muestra de 5 departamentos del pais;en cada departamento se debe 
# registrar 5 movimientos teluricos
# 1. cual es el departamento que tiene mayor riesgo de temblor
# 2. cual es el departamento que tiene menor riesgo de temblor
# 3. cual es el departamento que no tiene riesgo de temblor
# el riesgo es mayor si el promedio > 8.0
# si el promedio esta entre 3.0 y 7.9 es menor riesgo
# si el promedio es <3 no hay riesgo

totalDep = 5  
totalMuestras = 5  

depMayorRiesgo = ''
depMenorRiesgo = ''
depSinRiesgo = ''

mayorPromedio = 0
menorPromedio = 11  

for i in range(totalDep):
    nombreDEP = input(f"Ingrese el nombre del departamento Nro [{i+1}]: ")
    sumaSismos = 0  

    for j in range(totalMuestras):
        muestra = float(input(f"Ingrese la muestra del sismo [{j+1}] para el departamento [{nombreDEP}]: "))
        sumaSismos += muestra

    promedioSismos = sumaSismos / totalMuestras

    if promedioSismos > 8.0:
        if promedioSismos > mayorPromedio:
            mayorPromedio = promedioSismos
            depMayorRiesgo = nombreDEP
    elif 3.0 <= promedioSismos <= 7.9:
        if promedioSismos < menorPromedio:
            menorPromedio = promedioSismos
            depMenorRiesgo = nombreDEP
    elif promedioSismos < 3.0:
        if not depSinRiesgo:
            depSinRiesgo = nombreDEP
        else:
            depSinRiesgo += ', ' + nombreDEP

if depMayorRiesgo:
    print(f"El departamento con mayor riesgo de temblor es: {depMayorRiesgo} con un promedio de {mayorPromedio}")
else:
    print("No se encontraron departamentos con mayor riesgo de temblor.")

if depMenorRiesgo:
    print(f"El departamento con menor riesgo de temblor es: {depMenorRiesgo} con un promedio de {menorPromedio}")
else:
    print("No se encontraron departamentos con menor riesgo de temblor.")

if depSinRiesgo:
    print(f"Los departamentos que no tienen riesgo de temblor son: {depSinRiesgo}")
else:
    print("No hay departamentos sin riesgo de temblor.")