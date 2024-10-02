import os
from registro import equipo
from plantel import plantel 
import jugadores as jugadoresOptions
import registro 



lista_Jugadores=[
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
               menuJugadores(lista_Jugadores)
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


def menuJugadores(lista):
    while True:
        print("""
        MENU JUGADORES.
1. Agregar un jugador-
2. Eliminar un jugador.
3. Mostrar jugadores.
4. volver al menu princiapl.
""")
        opcion=input ("""INGRESE UNA OPCION: """)
        if (opcion=='1'):
            lista_Jugadores.append(jugadoresOptions.agregarJugadores(lista_Jugadores))
        elif (opcion =='2'):
            jugadoresOptions.eliminarJugador(lista)
        elif (opcion=='3'):
            jugadoresOptions.mostrarJugadores(lista)
        elif (opcion =='4'):
            print(menuPrincipal())
            return 
        else:
            print("opcion no valida, intente de nuevo")

            
if (__name__=="__main__"):
    menuPrincipal()


