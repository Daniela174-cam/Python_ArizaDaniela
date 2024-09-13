#Crea una calculadora que solicite dos números y una operación matemática (+, -, *, /). Usa match para realizar la operación correspondiente.
def calculadora (num1,num2,operacion):
    match operacion:
        case '+':
            return num1+num2
        case '-':
            return num1-num2
        case '*':
            return num1*num2
        case '/':
            return num1/num2
        case _: 
            return "operacion no valida"
        
num1 = float(input("ingrese primer numero: " ))
num2 = float(input("ingrese segundo numero: " ))
operacion = input("que tipo de operacion desea (+,-,*,/)") 
resultado = calculadora (num1,num2,operacion)
print ("el resultado es: ", resultado)