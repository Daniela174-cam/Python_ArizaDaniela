
nombre= str (input("ingrese nombre del jugador: "))
dorsal= int(input("ingrese dorsal del jugador: "))
posicion=str(input("ingrese la posicion del jugador: "))
golesJugador=int(input("ingrese cuantos goles hizo el jugador: "))
faltasJugador=int(input("cuantas faltas cometio el jugardor: "))
tarjetaA=int(input("cantidad de tarjetas amarillas: "))
tarjetaR=int(input("cantidad de tarjetas rojas: "))

def listaJugadores(diccionario):
    for i,e in diccionario.items():
        print('-----------------')
        print(f'{i}:{e}')
    

diccionario ={"nombre":nombre,"dorsal":dorsal,"posicion":posicion,"golesJugador":golesJugador,"faltasJugador":faltasJugador,"tarjetaA":tarjetaA,"tarjetaR":tarjetaR}

listaJugadores(diccionario)
    