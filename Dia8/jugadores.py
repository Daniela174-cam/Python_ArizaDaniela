def agregarJugadores(lista):
    while True:
        try: 
            nombre= input("ingrese nombre del jugador: ")
            jugador={
                "id": lista[-1]["id"] + 1, 
                "nombre": nombre
                          }
            print (jugador)
            return jugador
        
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
            print(f"Nombre: {jugador['nombre']}")        
        print("--------------------------")