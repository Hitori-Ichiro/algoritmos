num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese un operador (+, -, *, /): ")
if operador == '+':
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} es: {resultado}")
elif operador == '-':
    resultado = num1 - num2
    print(f"El resultado de {num1} - {num2} es: {resultado}")
elif operador == '*':
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} es: {resultado}")
elif operador == '/':
    if num2 == 0:
        print("Error: División por cero no permitida.")
    else:
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} es: {resultado}")
else:
    print("Operador no válido. Por favor ingrese uno de los siguientes: +, -, *, /.")