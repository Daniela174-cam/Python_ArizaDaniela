import os
from registro import equipo
from plantel import plantel 
from jugadores import eliminarJugador,anadir, listaJugadores as listaJ

listaJugadores=[
    {"id":1,"nombre": "juan"},
    {"id":2,"nombre": "ayu"}
]
listaPlantel=[
    {"nombre plantel":"fju"},
    {"nombre":2,"tecnico":"tecnico"}
]
listaEquipo=[
    {"nombre plantel":"fju"},
    {"nombre":2,"tecnico":"tecnico"}
]
def menuPrincipal():
    print("""
        LIGA BETPLAY
                                                                                      
    Opciones disponibles:
    1. menu jugadores.
    2. menu plantel.
    3. menu cuerpo tecnico.
    4. salir del programa.
""")
    print('-----------------')
    while True:
        try:
            opcion=input ("seleccione una opcion: ")
            if (opcion=='1'):
               anadir(listaJ)
            elif (opcion =='2'):
                plantel(listaPlantel)
            elif (opcion == '3'):
                equipo(listaEquipo)
            elif (opcion == '4'):
                print("Un gusto atenderte")
                break
            else:
               print("opcion no valida intenta de nuevo")
        except ValueError:
               print("Por favor, ingresa un número válido.")
        print('-----------------')


def menuInsert(listaJ):
       
       while True:
        print("""
    LISTA JUGADORES
                                                                                      
    Opciones disponibles:
    1. añadir jugador.
    2. eliminar jugador.
    3. mostrar lista de jugadores.
    4. salir del programa.
            """)
        try:
            opcion=input("seleccione una opcion: ")
            if opcion== '1':
                anadir()
            elif opcion=='2':
                eliminarJugador(listaJ)
            elif opcion== '3':
                listaJ(listaJ)
            elif opcion=='4':
                print("deseas volver al menu principal?")
                return
            else:
                print("opcion no valida,intente de nuevo")
        except ValueError:
            print(" ingresa un número válido.")
        except Exception as e:
            print(f"ha ocurrido un error: {e}")
            
menuPrincipal()     
        
    



