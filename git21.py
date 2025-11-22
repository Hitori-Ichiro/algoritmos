nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 60:
    print(f"Promedio: {promedio:.2f}. El estudiante aprueba.")
else:
    print(f"Promedio: {promedio:.2f}. El estudiante reprueba.")