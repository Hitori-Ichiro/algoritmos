num1 = int(input("Ingrese el primer numero: "))     
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
    print("Los tres numeros son pares.")
elif num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0:
    print("Los tres numeros son impares.")
else:
    print("Hay una mezcla de numeros pares e impares.")