#Crea un programa que solicite al usuario ingresar una contrasena y verifique si cumple con los siguientes
#requisitos: debe tener al menos 8 caracteres y contener al menos un numero. Si la contrasena cumple con
#los requisitos, muestra el mensaje"Contrasena valida". De lo contrario, muestra el mensaje "Contrasena invalida".

# Programa para verificar si una contraseña es válida
def es_contrasena_valida(contrasena):
    # Verificar si la longitud es al menos de 8 caracteres
    if len(contrasena) < 8:
        return False
    
    # Verificar si contiene al menos un número
    tiene_numero = any(char.isdigit() for char in contrasena)
    
    return tiene_numero

# Solicitar al usuario que ingrese una contraseña
contrasena = input("Ingresa una contraseña: ")

# Verificar si la contraseña es válida
if es_contrasena_valida(contrasena):
    print("Contraseña válida")
else:
    print("Contraseña inválida")
