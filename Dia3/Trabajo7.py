# Crea un programa que solicite al usuario ingresar tres longitudes y determine si esas longitudes pueden formar
# un triángulo válido. Utiliza la desigualdad triangular para realizar la comprobación y muestra un mensaje
# indicando si se puede formar un triángulo o no. La desigualdad triangular es un concepto matemático
# que establece una condición necesaria para que tres segmentos puedan formar un triángulo válido. La
# desigualdad triangular establece que la suma de las longitudes de dos lados de un triángulo siempre debe ser
# mayor que la longitud del tercer lado. En términos más precisos, si tienes tres segmentos con
# longitudes a, b y c, donde a, b y c son números
# positivos, entonces estos segmentos pueden formar un triángulo válido si y solo si se cumple la siguiente
# condición:
# a + b > c
# a + c > b
# b + c > a

# Si alguna de estas
# desigualdades no se
# cumple, entonces los
# segmentos no pueden
# formar un triángulo
# válido.

# La desigualdad
# triangular es un
# principio fundamental
# en la geometría y se
# utiliza para
# determinar la validez
# de un triángulo con
# base en las longitudes
# de sus lados.

# Función para determinar si las longitudes pueden formar un triángulo válido
def es_triangulo_valido(a, b, c):
    # Verificar la desigualdad triangular
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Solicitar al usuario que ingrese las tres longitudes
a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

# Verificar si se puede formar un triángulo válido
if es_triangulo_valido(a, b, c):
    print("Las longitudes ingresadas pueden formar un triángulo válido.")
else:
    print("Las longitudes ingresadas NO pueden formar un triángulo válido.")
    

# Explicación:
# La función es_triangulo_valido implementa la desigualdad triangular, que verifica si:
# 𝑎
# +
# 𝑏
# >
# 𝑐
# a+b>c
# 𝑎
# +
# 𝑐
# >
# 𝑏
# a+c>b
# 𝑏
# +
# 𝑐
# >
# 𝑎
# b+c>a
# Si todas las condiciones son verdaderas, las longitudes ingresadas pueden formar un triángulo.
# El programa solicita al usuario ingresar tres longitudes y luego llama a la función para verificar si las longitudes pueden formar un triángulo válido.
# Finalmente, se muestra un mensaje indicando si se puede o no formar un triángulo con esas longitudes.
# Este programa sigue el principio geométrico de la desigualdad triangular para validar la posibilidad de formar un triángulo.
