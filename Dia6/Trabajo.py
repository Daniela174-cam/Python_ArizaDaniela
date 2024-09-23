from jugadores import getPlayers, insertPlayer
from partidos import getPartidos, insertMatch
from equipoT import cuerpoTecnico,insertPlayer 

def menuPrincipal():
    while True:
        try:
            opcion=input ("""            
      LIGA BETPLAY
                                                                                      
    Opciones disponibles:
    1. menu jugadores.
    2. menu partidos.
    3. menu cuerpo tecnico.
                                                           

seleccione una opcion: """)
            if (opcion=='1'):
                menuJugadores()
            elif (opcion =='2'):
                menuPartidos()
            elif (opcion == '3'):
                menuTecnico()
            else:
                print("opcion no valida ")
        except:
            pass
        

def menuJugadores():
    
    opcion = input("""
    MENU JUGADORES

    1. obtener todos los jugadores.
    2. insertar un nuevo jugador.
Ingrese una opcion: """)
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
                   
    1. Obtener partidos.
    2. Insertar Partido
                   

Ingrese una opcion: """)
    
    try: 
        opcion = int(opcion)

    except ValueError:
        print('ingrese opcion valida pirobo')
        
def menuTecnico():
    
    opcion = input("""
    CUERPO TECNICO                                                                                                                                                     

    1. obtener todo el cuerpo tecnico.
    2. insertar nuevo tecnico.

Ingrese una opcion: """)
    try:
        opcion=int(opcion)
        if opcion == 1:
            cuerpoTecnico()
        elif opcion == 2:
            insertPlayer()
    except ValueError:
        print('acaso no lee las opciones imbecil?')
        menuTecnico()

menuPrincipal()

