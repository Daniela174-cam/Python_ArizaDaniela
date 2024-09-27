from jugadores import listaJugadores as listaJ
from registro import equipo
from plantel import plantel 


import os
listaOpciones:list
opciones:list
def crearmenu(listaOpciones,opciones):
    listaOpciones=['A' ,'B', 'F' ]
    opciones = ['A. Equipo goleador', 'B. Equipo más puntos' , 'F. Salir menú principal']
    os.system('clear')