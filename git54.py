calificacion = float(input("Ingrese la calificación (0-100): "))
if calificacion < 50:
    print("Muy deficiente")
elif 50 <= calificacion < 65:
    print("Deficiente")
elif 65 <= calificacion < 75:
    print("Regular")
elif 75 <= calificacion < 90:
    print("Buena")
else:
    print("Excelente")