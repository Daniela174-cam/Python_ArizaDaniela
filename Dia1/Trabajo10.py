#Solicita una nota numérica y clasifícala como A (90-100), B (80-89), C (70-79), D (60-69), o F (<60).

nota=int(input("ingrese su nota final: "))
if (90 <= nota <= 100):
    print("A")
elif (80 <= nota <= 89):
    print("B")
elif (70 <= nota <= 79):
    print("C")
elif (60 <= nota <= 69):
    print("D")
else:
    print("F")
