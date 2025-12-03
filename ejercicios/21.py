numeros = [5, 12, 3, 18, 25, 7]
valorDado = 10
contador = 0
for numero in numeros:
    if numero > valorDado:
        contador += 1
print("Cantidad de números mayores que", valorDado, ":", contador)
