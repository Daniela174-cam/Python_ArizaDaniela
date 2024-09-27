
lugar=str(input("ingrese nombre del plantel: "))
local=bool(input("es ud local s(si) N(no): "))
fecha=(input("ingrese fecha del juego: "))

def plantel(diccionario):
    for i,e in diccionario.items():
        print(f'{i}:{e}')


diccionario ={"lugar":lugar,"local":local,"fecha":fecha}

plantel(diccionario)
