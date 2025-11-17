#Escribe un programa que le pida al usuario su calificación y determine si aprobó o reprobó y si es una aprobado especial
calificacion = float(input("Ingrese su calificación: "))
if calificacion >= 60:
    if calificacion >= 90:
        print("Aprobado especial")
    else:
        print("Aprobado")
else:
    print("Reprobado")
    