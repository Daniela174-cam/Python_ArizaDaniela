#En su casa le solicitan que realice un algoritmo en Python,que permita calcular el valor a pagar por concepto de energia
#electrica. Los datos que se conocen son los siguientes:
#-Mes de consumo
#-Valorkw
#-Totalkwconsumido en el mes-estrato

# Función para calcular el valor a pagar por energía eléctrica
def calcular_valor_pago(valor_kw, total_kw, estrato):
    # Definir el factor de ajuste según el estrato
    if estrato == 1:
        descuento = 0.6  # 40% de descuento
    elif estrato == 2:
        descuento = 0.85  # 15% de descuento
    elif estrato == 3:
        descuento = 1.0  # Sin ajuste
    elif estrato == 4:
        aumento = 1.05  # 5% de aumento
    elif estrato == 5:
        aumento = 1.1   # 10% de aumento
    elif estrato == 6:
        aumento = 1.15  # 15% de aumento
    else:
        return "Estrato no válido"

    # Calcular el valor básico
    valor_basico = valor_kw * total_kw

    # Aplicar el ajuste de precio según el estrato
    if estrato in [1, 2]:
        valor_total = valor_basico * descuento
    else:
        valor_total = valor_basico * aumento
    
    return valor_total

# Solicitar al usuario ingresar los datos
mes = input("Ingresa el mes de consumo: ")
valor_kw = float(input("Ingresa el valor por kW: "))
total_kw = float(input("Ingresa el total de kW consumidos: "))
estrato = int(input("Ingresa el estrato del hogar (1-6): "))

# Calcular el valor a pagar
valor_a_pagar = calcular_valor_pago(valor_kw, total_kw, estrato)

# Mostrar el resultado
if isinstance(valor_a_pagar, str):
    print(valor_a_pagar)  # Mensaje de error si el estrato no es válido
else:
    print(f"El valor a pagar en el mes de {mes} es: ${valor_a_pagar:.2f}")
