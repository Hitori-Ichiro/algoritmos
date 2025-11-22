#Pide una temperatura y clasifícala como "Muy frío", "Frío", "Tibio", "Caliente", o "Muy caliente".
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
if temperatura < 0:
    print("muy frío")
elif 0 <= temperatura < 15:
    print("frío")
elif 15 <= temperatura < 25:
    print("normal")
elif 25 <= temperatura < 35:
    print("Calor")
else:
    print("Mucho calor")