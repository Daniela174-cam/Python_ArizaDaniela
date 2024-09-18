#Crea un programa que pida al usuario ingresar el nombre de un pais y luego determine en que continente se encuentra.
#Utiliza estructuras condicionales para asociar cada pais con su respectivo continente y muestra un mensaje con el
#continente correspondiente.

# Programa para determinar el continente de un país
def determinar_continente(pais):
    # Listas de países por continente
    america = ['canada', 'mexico', 'argentina', 'brasil', 'chile', 'colombia']
    europa = ['españa', 'francia', 'alemania', 'italia', 'portugal', 'reinounido']
    asia = ['china', 'japon', 'india', 'corea', 'tailandia', 'rusia']
    africa = ['nigeria', 'sudafrica', 'kenia', 'egipto', 'marruecos', 'etiopia']
    oceania = ['australia', 'nuevazelanda', 'fiyi', 'papuanuevaguinea', 'samoa']

    # Convertir el nombre del país a minúsculas para evitar problemas de capitalización
    pais = pais.lower()

    # Verificar en qué continente está el país
    if pais in america:
        return "América"
    elif pais in europa:
        return "Europa"
    elif pais in asia:
        return "Asia"
    elif pais in africa:
        return "África"
    elif pais in oceania:
        return "Oceanía"
    else:
        return "País no reconocido"

# Solicitar al usuario que ingrese el nombre de un país
pais = input("Ingresa el nombre de un país: ")

# Determinar el continente del país
continente = determinar_continente(pais)

# Mostrar el continente
print(f"El país {pais.title()} se encuentra en {continente}.")
