total = 0
for i in range(5):
    calificacion = float(input(f"Ingrese la calificación {i+1}: "))
    total += calificacion
promedio = total / 5
if promedio < 6:
    print("Desempeño bajo")
elif 6 <= promedio < 8:
    print("Desempeño medio")
else:
    print("Desempeño alto")