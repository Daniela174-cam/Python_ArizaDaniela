from jugadores import getPlayers, insertPlayer
from partidos import getPartidos, insertMatch

def menuPrincipal():
    while True:
        try:
            opcion=input ("""            
▗▖   ▗▄▄▄▖ ▗▄▄▖ ▗▄▖     ▗▄▄▖ ▗▄▄▄▖▗▄▄▄▖▗▄▄▖ ▗▖    ▗▄▖▗▖  ▗▖
▐▌     █  ▐▌   ▐▌ ▐▌    ▐▌ ▐▌▐▌     █  ▐▌ ▐▌▐▌   ▐▌ ▐▌▝▚▞▘ 
▐▌     █  ▐▌▝▜▌▐▛▀▜▌    ▐▛▀▚▖▐▛▀▀▘  █  ▐▛▀▘ ▐▌   ▐▛▀▜▌ ▐▌  
▐▙▄▄▖▗▄█▄▖▝▚▄▞▘▐▌ ▐▌    ▐▙▄▞▘▐▙▄▄▖  █  ▐▌   ▐▙▄▄▖▐▌ ▐▌ ▐▌  
                                                                                      
    Opciones disponibles:
    1. menu jugadores.
    2. menu partidos
                                                           

seleccione una opcion: """)
            if (opcion=='1'):
                menuJugadores()
            elif (opcion =='2'):
                menuPartidos()
            else:
                print("opcion no valida ")
        except:
            pass
        

def menuJugadores():
    
    opcion = input("""
                   
▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖▗▖ ▗▖       ▗▖▗▖ ▗▖ ▗▄▄▖ ▗▄▖ ▗▄▄▄  ▗▄▖ ▗▄▄▖ ▗▄▄▄▖ ▗▄▄▖
▐▛▚▞▜▌▐▌   ▐▛▚▖▐▌▐▌ ▐▌       ▐▌▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌  █▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌   
▐▌  ▐▌▐▛▀▀▘▐▌ ▝▜▌▐▌ ▐▌       ▐▌▐▌ ▐▌▐▌▝▜▌▐▛▀▜▌▐▌  █▐▌ ▐▌▐▛▀▚▖▐▛▀▀▘ ▝▀▚▖
▐▌  ▐▌▐▙▄▄▖▐▌  ▐▌▝▚▄▞▘    ▗▄▄▞▘▝▚▄▞▘▝▚▄▞▘▐▌ ▐▌▐▙▄▄▀▝▚▄▞▘▐▌ ▐▌▐▙▄▄▖▗▄▄▞▘
                                                                       
                                                                                                                       
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

▗▄▄▖  ▗▄▖ ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▄▄▄  ▗▄▖  ▗▄▄▖
▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌ █    █  ▐▌  █▐▌ ▐▌▐▌   
▐▛▀▘ ▐▛▀▜▌▐▛▀▚▖ █    █  ▐▌  █▐▌ ▐▌ ▝▀▚▖
▐▌   ▐▌ ▐▌▐▌ ▐▌ █  ▗▄█▄▖▐▙▄▄▀▝▚▄▞▘▗▄▄▞▘
                                                                                                                     
    Menu Partidos
                   
Ingrese una opcion: 
    1. Obtener partidos.
    2. Insertar Partido
                   
""")
    
    try: 
        opcion = int(opcion)

    except ValueError:
        print('ingrese opcion valida pirobo')
        


menuPrincipal()

