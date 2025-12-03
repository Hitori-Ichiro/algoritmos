def contarVocales(palabra):
    vocales = "aeiou"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador
palabra = "tecnologia"
print(f"La palabra '{palabra}' tiene {contarVocales(palabra)} vocales.")
