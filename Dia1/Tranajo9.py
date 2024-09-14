# Solicita la edad de la persona e indica si es niño (0-12 años), adolescente (13-17 años), adulto (18-
# 64 años) o anciano (65 años o más).
edad=int(input("ingrese su edad: "))
if 0 <= edad <= 12:
    print("Es niño")
elif 13 <= edad <= 17:
    print("es adolecente")
elif 18 <= edad <= 64:
    print("adulto")
else:
    print("anciano")

    