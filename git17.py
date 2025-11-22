num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num2 != 0:
    if num1 % num2 == 0:
        print(f"El número {num1} es múltiplo de {num2}.")
    else:
        print(f"El número {num1} no es múltiplo de {num2}.")
else:

    print("Error: No se puede dividir por cero.")