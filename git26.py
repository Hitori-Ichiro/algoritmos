horasTrabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
tarifaHora =6.189
if horasTrabajadas <= 44:
    salario = horasTrabajadas * tarifaHora
else:
    horasExtras = horasTrabajadas - 40
    salario = (44 * tarifaHora) + (horasExtras * tarifaHora * 1.5)
print(f"El salario semanal es: ${salario:.2f}")