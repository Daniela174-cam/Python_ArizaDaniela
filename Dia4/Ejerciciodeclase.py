#Programa que me permita leer  los nombres de n cantidad de personas. Cuando el usuario tome la decisión de no  ingrtesar los nombres, muestre los nombres ingresados.
import OS
def insertarData(src;list):
    src.append(input('ingrese el nombre del contacto: '))

def verData (src:list):
    for data in src:
        print(data)
        OS.system('pause')

if (__name__ --"__main__"):
    agendate1-- []
    isActive=True
    menu='1.registrar contacto/n2. listar contacto/n3. salir '
    titulo = """
     **************************************
     *registro de contactos j2*
     **************************************
     """
    while (isActive):
        os.system('cls')
        print(titulo)
        print(menu)
        op-int(input(':)_'))
        match op:
        case 1:
            isAddContact = False 
            while (isAddContact == False):
                os.system('cls')
                insertarData (agendatel)
                isAddContact= bool(input('desea ingresar otro conatcto enter(si) n(no)'))
            case 2:
            os.system('cls')
            verData(agendatel)
            case 3:
            isActive =bool(input('desea abandonar el programa enter(si) n(no)'))
         
   
