

def equipo(lista):

    while True:
        try:
        
            equipos =(input("ingrese nombre del equipo: "))

            diccionario ={
            "id": lista[-1]["id"] + 1, 
            "equipos":equipos,"dorsal":dorsal,
            "posicion":posicion,
            "golesJugador":golesJugador,
            "faltasJugador":faltasJugador,
            "tarjetaA":tarjetaA,
            "tarjetaR":tarjetaR
            }
            print (diccionario)
            return diccionario
        except ValueError:
            print("porfavor intente de nuevo")

    
def eliminarEquipo(lista):
    nombre = input("Ingrese el nombre del equipo  que desea eliminar: ")
    
    equipo_encontrado = False
    for equipo in lista:

        if equipo['nombre'].lower() == nombre.lower():
            lista.remove(equipo)

            print(f"El equipo {nombre} ha sido eliminado.")
            equipo_encontrado = True
            break

    if not equipo_encontrado:
        print(f"No se encontró al equipo con nombre {nombre}.")


def mostrarEquipo(listaE):
    if not listaE:
        print("No hay equipos en la lista.")
    else:
        print("Lista de equipos")
        for jugador in listaE:
            print(f"Nombre: {jugador['nombre']}, "
                  f"Dorsal: {jugador['dorsal']}, "
                  f"Posición: {jugador['posicion']}, "
                  f"Goles: {jugador['golesJugador']}, "
                  f"Faltas: {jugador['faltasJugador']}, "
                  f"Tarjetas Amarillas: {jugador['tarjetaA']}, "
                  f"Tarjetas Rojas: {jugador['tarjetaR']}")        
        print("--------------------------")



