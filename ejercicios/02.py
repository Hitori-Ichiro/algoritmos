def segundoGrande(lista):
    primero = segundo = float('-inf')
    for numero in lista:
        if numero > primero:
            segundo = primero
            primero = numero
        elif primero > numero > segundo:
            segundo = numero
    return segundo
numeros = [10, 15, 20, 25, 5]
resultado = segundoGrande(numeros)
print("El segundo número más grande es:", resultado)