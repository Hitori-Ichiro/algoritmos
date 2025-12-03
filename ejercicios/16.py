def invertirCadena(cadena):
    cadenaInvertida = ""
    for caracter in cadena:
        cadenaInvertida = caracter + cadenaInvertida
    return cadenaInvertida

texto = "la meta es el rango radiante"
resultado = invertirCadena(texto)
print("Cadena original:", texto)
print("Cadena invertida:", resultado)