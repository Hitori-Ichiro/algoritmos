def invertirLista(lista):
    listaInvertida = []
    for elemento in lista:
        listaInvertida.insert(0, elemento)
    return listaInvertida
numeros = [1, 2, 3, 4, 5]
resultado = invertirLista(numeros)
print("Lista invertida:", resultado)