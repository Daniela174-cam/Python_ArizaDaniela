from data import st

campus= {}
isAddCamper=True
menu = ('1.Add Camper', '2. Exit')
while isAddCamper:
    for item in menu:
        print(item)
    op=int(input(' :)_'))
    match op:
        case 1:
            st.camper['nombre']= input ('ingrese el nombre del estudiante: ')
            codigo=str(len(campus)+1).zfill(6);
            campus.update({codigo:st.camper})
            isAddCamper=bool(input('presione enter àra salir o cualquier otra cosa para continuar: '))
        case _:
            print('erroorr')
print (campus)
