#Construya un algoritmo en Python, que permita ingresar la informacion de un empleado e imprima el nombre, los apellidos
#y la antigüedad. Los datos que se deben solicitarson los siguientes:
#*Nombre* Teléfono
#*Año de ingreso a la empresa*Apellidos
#*Edad.

nombre=str(input("ingrese su nombre: "))
apellido=str(input("ingrese su apellido: "))
edad=int(input("ingrese su edad: "))
telefono=int(input("ingrese su numero de telefono: "))
antiguedad=float(input("cuanto tiempo me llevas dando tu vida?: "))

def listaInformacion(diccionario):
    for i, e in diccionario.items():
        print(f'{i}: {e}')
        
diccionario={"nombre":nombre  ,"apellido":apellido, "telefono":telefono ,"antiguedad":antiguedad ,"edad":edad}

listaInformacion(diccionario)
