

def plantel(lista):
    nombreE = input("Ingrese el nombre del jugador que desea eliminar: ")
    jugador={
                "id": lista[-1]["id"] + 1, 
                "nombre": nombreE, 
                }


def registrarEquipo(lista):

    lugar=str(input("ingrese nombre del plantel: "))
    local=bool(input("es ud local s(si) N(no): "))
    fecha=(input("ingrese fecha del juego: "))
    golesAfavor=int(input("ingrese la cantidad de goles del equipo: "))
    golesEnContra=int(input("ingrese la cantidad de goles que le hicieron: "))

    
    jugador_encontrado = False
    for jugador in lista:

        if nombreE['nombre'].lower() == nombreE.lower():
            lista.remove(jugador)

            print(f"El jugador {nombreE} ha sido eliminado.")
            jugador_encontrado = True
            break

    if not jugador_encontrado:
        print(f"No se encontró al jugador con nombre {nombreE}.")

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