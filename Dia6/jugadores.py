jugadores =[

]

def getPlayers(): 
    for i in jugadores:
        jugador = i
        for a,e in jugador.items():
            print(f'{a}:{e}')
        print('------------------------')        
   
# getPlayers()

def insertPlayer():
    nombre = input(f'ingrese nombre del jugador: ')
    numero = input(f'numero del jugador: ')
    posicion = input(f'posicion del jugador: ')
    print('------------------------') 

    newPlayer = {
        "nombre":nombre,
        "numero":numero,
        "posicion":posicion
    }

    jugadores.append(newPlayer)
    getPlayers()
# insertPlayer()



