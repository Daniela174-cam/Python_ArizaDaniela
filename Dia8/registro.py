
equipos =(input("ingrese nombre del equipo: "))
golesAfavor= (input("ingrese la cantidad de goles del equipo: "))
golesEnContra=(input("ingrese la cantidad de goles que le hicieron: "))

def equipo(diccionario):
    for i,e in diccionario.items():
        print('-----------------')
        print(f'{i}:{e}')

diccionario ={"equipos":equipos,"golesAf":golesAfavor,"golesEnContra":golesEnContra}

equipo(diccionario)