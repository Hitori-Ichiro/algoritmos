num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
distancia1 = abs(100 - num1)
distancia2 = abs(100 - num2)
if distancia1 < distancia2:
    print(f"El número {num1} está más cerca de 100.")
elif distancia2 < distancia1:
    print(f"El número {num2} está más cerca de 100.")
else:
    print("Ambos números están a la misma distancia de 100.")