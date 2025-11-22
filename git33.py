puntaje = float(input("Ingrese el puntaje del examen (0-20): "))
if 18<= puntaje <= 20:
    print("Calificación: A")
elif 16 <= puntaje < 17:
    print("Calificación: B")
elif 14 <= puntaje < 15:
    print("Calificación: C")
elif 11 <= puntaje < 13:
    print("Calificación: D")
else:
    print("Calificación: F")