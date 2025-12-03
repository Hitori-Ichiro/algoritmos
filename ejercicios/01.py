def imprimirNumerosTriangulares(n):
    for i in range(1, n + 1):
        numeroTriangular = (i * (i + 1)) // 2
        print(numeroTriangular)
imprimirNumerosTriangulares(10)
