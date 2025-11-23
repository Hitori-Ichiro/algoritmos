diaSemana = input("Ingrese un día de la semana: ").strip().lower()
if diaSemana in ["sábado", "domingo"]:
    print("Es fin de semana.")
else:
    print("Es un día laboral.")