
jugador1= input("ingrese su nombre: ")
jugador2=input ("ingrese su nombre: ")
apodo=input("ingrese un apodo por favor: ")


jugador_encontrado = False
for jugador in lista:

        if jugador['nombre'].lower() == jugador.lower():
            lista.remove(jugador)

            print(f"El jugador {jugador} ha sido eliminado.")
            jugador_encontrado = True
            break

if not jugador_encontrado:
        print(f"No se encontró al jugador con nombre {jugador}.")