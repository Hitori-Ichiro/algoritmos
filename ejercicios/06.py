frase = "ya pagaron"
palabras = frase.split()
for palabra in palabras:
    primeraLetra = palabra[0]
    ultimaLetra = palabra[-1]
    print(f"Palabra: {palabra}, Primera letra: {primeraLetra}, Última letra: {ultimaLetra}")