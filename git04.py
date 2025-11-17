calificacion = float(input("Ingrese su calificación: "))
if calificacion >= 60:
    if calificacion >= 90:
        print("Aprobado especial")
    else:
        print("Aprobado")
else:
    print("Reprobado") 