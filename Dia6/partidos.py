from datetime import datetime

partidos =[
    {
        "id":1, 
        "fecha":'2024-09-21 16:53:24.366903',
        "equipo_visitante": "los peperolos",
        "equipo_local": "ayus",
        "estadio": " estadio de venezuela",
        "goles_visitante":0,
        "goles_local":0,
    }
]

def getPartidos():
    for i in partidos:
        partido = i
        for a,e in partido.items():
            print(f'{a}:{e}')
        print('------------------')

def insertMatch():
    visitante = input('equipo visitante: ')
    local = input('equipo local: ')
    estadio = input('nombre estadio: ')
    ultimoId = partidos[-1].id
    match = {
        "id": ultimoId + 1, 
        "fecha": datetime.now(),
        "equipo_visitante": visitante,
        "equipo_local": local,
        "estadio": estadio,
        "goles_visitante":0,
        "goles_local":0,
    }

    partidos.append()
    getPartidos()
