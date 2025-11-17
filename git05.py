num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
operador = input("Ingrese un operador (+, -, *, /): ")
if operador == "+":
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} es: {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"El resultado de {num1} - {num2} es: {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} es: {resultado}")
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    else:
        print("Error: division por cero no permitida.")
else:
    print("Operador no valido.")