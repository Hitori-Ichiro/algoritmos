calificacion = float(input("Ingrese una calificación (0-5): "))
if calificacion >= 4.5 and calificacion <= 5:
    print("Excelente")
elif calificacion >= 4 and calificacion < 4.5:
    print("Buena")
elif calificacion >= 3 and calificacion < 3.9:
    print("Regular")
elif calificacion >= 0 and calificacion < 2.9:
    print("Mala")
else:
    print("Calificación inválida")