tarea = float(input("Ingrese la calificación de la tarea (0-100): "))
proyecto = float(input("Ingrese la calificación del proyecto (0-100): "))
examen = float(input("Ingrese la calificación del examen (0-100): "))
notaFinal = (tarea * 0.3) + (proyecto * 0.4) + (examen * 0.3)
if notaFinal >= 90:
    print("A")
elif 80 <= notaFinal < 90:
    print("B")
elif 70 <= notaFinal < 80:
    print("C")
elif 60 <= notaFinal < 70:
    print("D")
else:
    print("F")
    