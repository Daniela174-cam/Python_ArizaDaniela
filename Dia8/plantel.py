

def plantel(lista):

    lugar=str(input("ingrese nombre del plantel: "))
    local=bool(input("es ud local s(si) N(no): "))
    fecha=(input("ingrese fecha del juego: "))
    golesAfavor=int(input("ingrese la cantidad de goles del equipo: "))
    golesEnContra=int(input("ingrese la cantidad de goles que le hicieron: "))
    diccionario ={"lugar":lugar,"local":local,"fecha":fecha,"golesAfavor":golesAfavor,"golesEnContra": golesEnContra}
    for i,e in diccionario.items():
        print('-----------------')
        print(f'{i}:{e}')
    lista.append(diccionario)
