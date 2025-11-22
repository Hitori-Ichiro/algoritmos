temperaturaC = float(input("Ingrese la temperatura en grados Celsius: "))
unidadDestino = input("Ingrese la unidad a convertir (F para Fahrenheit, K para Kelvin): ").upper()
if unidadDestino == 'F':
    temperaturaF = (temperaturaC * 9/5) + 32
    print(f"La temperatura en Fahrenheit es: {temperaturaF:.2f} °F")    
elif unidadDestino == 'K':
    temperaturaK = temperaturaC + 273.15
    print(f"La temperatura en Kelvin es: {temperaturaK:.2f} K")
else:
    print("Unidad no válida. Por favor ingrese 'F' o 'K'.")