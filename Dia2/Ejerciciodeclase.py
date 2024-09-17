
sumaNota=0.0

def leerNotas(totalNotas:int,titulo:str):
    nota = 0.0
    contadorNotas = 1
    while (totalNotas > 0):
        nota += float(input(f'Ingrese la nota Nro {contadorNotas} de {titulo} :'))
        contadorNotas +=1
        totalNotas -=1

def leerNotasRecursiva(totalNotas:int,titulo:str,nota:float,totalNotasActual:int):
    global sumaNota 
    if totalNotas==1:
        sumaNota=0
    nota += float(input(f'Ingrese la nota Nro {totalNotasActual} de {titulo} :'))

    sumaNota = nota

    totalNotasActual +=1


    if(totalNotasActual<=totalNotas):
        leerNotasRecursiva(totalNotas,titulo,sumaNota,totalNotasActual)

    return sumaNota/totalNotas



if (__name__ == "__main__"):
    sumaParciales = 0.0
    sumaQuices = 0.0
    sumaTrabajos = 0.0
    # leerNotas(2,'Parciales')
    # leerNotas(3,'Quices')
    # leerNotas(1,'Trabajos')
    sumaParciales = leerNotasRecursiva(3,'Parciales',0.0,1)
    sumaQuices = leerNotasRecursiva(4,'Quices',0.0,1)
    sumaTrabajos = leerNotasRecursiva(2,'Trabajos',0.0,1)

    print(f'su nota final es: {((sumaParciales*0.6)+ (sumaQuices*0.3)+(sumaTrabajos*0.1))}' )