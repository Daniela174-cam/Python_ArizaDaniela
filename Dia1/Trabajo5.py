#Solicita al usuario un número del 1 al 7 y muestra el día de la semana correspondiente (1 = Lunes,
# 7 = Domingo).

def DiasDeLaSemana (dias):
    match str (dias):
        case '1':
            return "lunes"
        case '2':
            return "martes"
        case '3':
            return "miercoles"
        case '4':
            return "jueves" 
        case '5':
            return "viernes" 
        case '6':
            return "sabado" 
        case '7':
            return "domingo"
        case _:
            return "error"
dias = int(input("ingrese un numero del 1 al 7: "))
semana= DiasDeLaSemana (dias)
print ("el dia de la semana es: " , semana)



