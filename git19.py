velocidad = float(input("Ingrese la velocidad en km/h: "))
if velocidad < 40:
    print("Velocidad Baja")
elif 40 <= velocidad <= 80:
    print("Velocidad Normal")
else:
    print("Velocidad Alta")
    