# Escribe un programa que calcule el costo de estacionamiento basado en el número de horas, con
# tarifas progresivas.
# El costo de estacionamiento se calcula de la siguiente manera:
# Primera hora: $5
# Segunda a cuarta hora: $4 por hora
# Más de cuatro horas: $3 por cada hora adicional
# Solicita al usuario el número de horas de estacionamiento y calcula el costo total.

num_horas = float(input("Ingrese número de horas en el estacionamiento: "))

costo_total = 0

for i in range(int(num_horas)):
    if num_horas == 1:
        costo_total += 5
    elif 2 <= num_horas <= 4:
        costo_total += 4
    else:
        costo_total += 3

if num_horas % 1 > 0:   
    if num_horas <= 1:
        pass
    elif num_horas <= 4:
        costo_total += (num_horas % 1) * 4
    else:
        costo_total += (num_horas % 1) * 3
        
print(f"Su costo total del feo y caro estacionamiento de zona franca es de: {costo_total} pesos mi perro")

