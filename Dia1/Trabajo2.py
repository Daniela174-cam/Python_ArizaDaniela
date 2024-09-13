#Solicita al usuario una calificación y determina si la nota es aprobatoria (>= 60) o reprobatoria (<60)

nota= int(input("ingrese nota final: "))
aprobado= nota>60
reprobado=nota<60
porLosPelos = nota >= 65 and nota <=70
if aprobado:
        if porLosPelos:
            print("Por los pelos viejo, casi te filtra johlver")
        else:
            print("Felicidades, has aprobado")
else:
    print("rayos viejo, te filtraron ")