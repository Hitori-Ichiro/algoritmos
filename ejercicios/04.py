def eliminarDuplicados(lista):
    return list(set(lista))
lista = [1, 2, 2, 3, 4, 4, 5]
resultado = eliminarDuplicados(lista)
print("Lista sin duplicados:", resultado)