def agregarJugadores(lista):
    while True:
        try: 
            nombre= input("ingrese nombre del jugador: ")
            #dorsal= int(input("ingrese dorsal del jugador(numero): "))
            #posicion=input("ingrese la posicion del jugador: ")
            #golesJugador=int(input("ingrese cuantos goles hizo el jugador: "))
            #faltasJugador=int(input("cuantas faltas cometio el jugardor: "))
            #tarjetaA=int(input("cantidad de tarjetas amarillas: "))
            #tarjetaR=int(input("cantidad de tarjetas rojas: "))
            jugador={
                "id": lista[-1]["id"] + 1, 
                "nombre": nombre,
     #           "dorsal":dorsal,
      #          "posicion":posicion,
   #             "golesJugador":golesJugador,
      #          "faltasJugador":faltasJugador,
      #          "tarjetaA":tarjetaA,
 #               "tarjetaR":tarjetaR
                          }
            print (jugador)
            return jugador
            #print(f"Jugador {nombre} agregado correctamente.\n")
            return
        except ValueError:
            print("porfavor intente de nuevo")
    


def eliminarJugador(lista):
    nombre = input("Ingrese el nombre del jugador que desea eliminar: ")
    
    jugador_encontrado = False
    for jugador in lista:

        if jugador['nombre'].lower() == nombre.lower():
            lista.remove(jugador)

            print(f"El jugador {nombre} ha sido eliminado.")
            jugador_encontrado = True
            break

    if not jugador_encontrado:
        print(f"No se encontró al jugador con nombre {nombre}.")

def mostrarJugadores(listaJ):
    if not listaJ:
        print("No hay jugadores en la lista.")
    else:
        print("--- Lista de Jugadores ---")
        for jugador in listaJ:
            print(f"Nombre: {jugador['nombre']}, "
                  f"Dorsal: {jugador['dorsal']}, "
                  f"Posición: {jugador['posicion']}, "
                  f"Goles: {jugador['golesJugador']}, "
                  f"Faltas: {jugador['faltasJugador']}, "
                  f"Tarjetas Amarillas: {jugador['tarjetaA']}, "
                  f"Tarjetas Rojas: {jugador['tarjetaR']}")        
        print("--------------------------")