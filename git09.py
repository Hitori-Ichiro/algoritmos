import math
num = float(input("Ingrese un numero: "))
if num >= 0:
    raiz = math.sqrt(num)
    print(f"La raíz cuadrada de {num} es {raiz}")
else:
    print("Error: No se puede calcular la raíz cuadrada de un numero negativo.")