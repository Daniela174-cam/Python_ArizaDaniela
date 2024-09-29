

def equipo(lista):
    equipos =(input("ingrese nombre del equipo: "))
   
    diccionario ={"equipos":equipos,}
    lista.append(diccionario)
    for i,e in diccionario.items():
        print('-----------------')
        print(f'{i}:{e}')


def insertPlayer(lista):
    print("Añadiendo jugadores...")
    equipo(lista)  

    print("\nJugadores añadidos al equipo:")
    for jugador in lista:
        print(jugador)



