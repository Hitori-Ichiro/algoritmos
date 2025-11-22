diasRetraso = int(input("Ingrese el número de días de retraso en la devolución del libro: "))
if diasRetraso <= 0:
    print("No hay multa.")
elif 1 <= diasRetraso <= 5:
    multa = diasRetraso * 0.50
    print(f"La multa es de ${multa:.2f}.")
elif 6 <= diasRetraso <= 10:
    multa = diasRetraso * 1.00
    print(f"La multa es de ${multa:.2f}.")
else:
    multa = diasRetraso * 2.00
    print(f"La multa es de ${multa:.2f}.")
