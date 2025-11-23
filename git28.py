mes = input("Ingrese el mes (en minúsculas): ")
cicloEscolar = ['septiembre', 'octubre', 'noviembre', 'diciembre', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
if mes in cicloEscolar:
    print(f"El mes de {mes} está dentro del ciclo escolar.")
else:
    print(f"El mes de {mes} está en vacaciones.")