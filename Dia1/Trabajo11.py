#Solicita al usuario que ingrese una temperatura y una escala (C o F). Convierte la temperatura a la
# escala opuesta usando match .
def termometro (grados, temperatura):
    match str (grados):
        case 'Fahrenheit':
            return (temperatura - 32) * 5/9
        case 'Celsius':
            return (temperatura * 9/5) + 32
        case _: 
            return "operacion no valida"
        
temperatura = float(input("ingrese el numero de grados: " ))
grados = input("que tipo de convercion desea (Celsius , Fahrenheit): ") 
resultado = termometro (grados, temperatura)
print ("el resultado de la convercion es: ", resultado)