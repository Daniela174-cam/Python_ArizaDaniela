# # #El instituto nacional de sismologia desea una muestra de 5 departamentos del pais;en cada departamento se debe 
# # registrar 5 movimientos teluricos
# # 1. cual es el departamento que tiene mayor riesgo de temblor
# # 2. cual es el departamento que tiene menor riesgo de temblor
# 3. cual es el departamento que no tiene riesgo de temblor
# el riesgo es mayor si el promedio >8.0
# si el promedio esta entre 3.0 y 7.9 es menor riesgo
# si el promedio es >3 no hay riesgo 

promedioSismos=0
totalDep= 2
totalMuestras=2
contadorMuestras=0
depMayorRiesgo= ''
depMenorRiesgo=''
depSinRiesgo=''

for i in range(0,totalDep):
    nombreDEP= input(f"ingrese el nombre del departamento Nro [{i+1}]: ")
    while( contadorMuestras<totalMuestras):
        muestra=float (input (f"ingrese la muestra del sismo para el departamento [{nombreDEP}]: "))
        promedioSismos /= totalMuestras
        contadorMuestras+1
        if promedioSismos >= 8.0:
            pass
        elif promedioSismos>= 3.0 and promedioSismos < 8.0:
            pass
        else:
            pass
        contadorMuestras=0

promedioSismos= + totalMuestras
avg = sum_num / len(num)
