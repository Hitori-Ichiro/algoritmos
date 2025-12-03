def contarLetras(cadena):
    conteo = {}
    for caracter in cadena:
        if caracter.isalpha(): 
            caracter = caracter.lower()  
            if caracter in conteo:
                conteo[caracter] += 1
            else:
                conteo[caracter] = 1
    return conteo
texto = "lenovo es la marca de mi laptop"
resultado = contarLetras(texto)
print("Conteo de letras:", resultado)