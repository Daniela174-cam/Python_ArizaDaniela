# Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario
# adivinarlo. El programa debe dar pistas si el número ingresado es mayor o menor que el número
# secreto. Usa un ciclo while para permitir al usuario seguir intentando hasta que adivine el
# número
import random

numero_secreto = random.randint(1, 100)

print("Mi perro, si adivina el número no lo filtro ¡juaz juaz juaz juaz!")

adivinanza = None

while adivinanza != numero_secreto:
    adivinanza = int(input("A ver socio, cual pensó, sueltelo ahí: "))
    
    if adivinanza < numero_secreto:
        print("No perro, hechele mas, que eso no llega")
    elif adivinanza > numero_secreto:
        print("Se pasó mi perro, asi tampoco")
    else:
        print(f"Le dió al clavo socio, asi es que es, la buena, siga en campus, el numero si era: {numero_secreto}.")