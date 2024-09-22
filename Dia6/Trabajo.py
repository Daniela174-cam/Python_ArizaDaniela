from jugadores import getPlayers, insertPlayer
from partidos import getPartidos, insertMatch


def menuJugadores():
    
    opcion = input("""
Ingrese una opcion:
    1. obtener todos los jugadores.
    2. insertar un nuevo jugador.
""")
    try:
        opcion=int(opcion)
        if opcion == 1:
            getPlayers()
        elif opcion == 2:
            insertPlayer()
        elif opcion==3:
            menuPartidos()
        else:
            print('opcion no valida pedazo de popo')
            menuJugadores()
    except ValueError:
        print('acaso no lee las opciones imbecil?')
        menuJugadores()

    

def menuPartidos():
    opcion = input("""
        Menu Partidos
                   
Ingrese una opcion: 
    1. Obtener partidos.
    2. Insertar Partido
                   
""")
    
    try: 
        opcion = int(opcion)

    except ValueError:
        print('ingrese opcion valida pirobo')
        
        
def menu():
    opcion = input("""
 Menu LigBetPlay
    1. Menu Juadores
    2. Menu partidos.
""")
    try:
        opcion = int(opcion)

        if opcion == 1 :
            menuJugadores()
        if opcion == 2:
            pass
            # menuPartidos()
        else:
            print(' opcion invalida')
            menu()
    
    except ValueError:
        print('ingresar solo numeros')
        menu()


menuJugadores()