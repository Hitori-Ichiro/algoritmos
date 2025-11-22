tipoSangre = input("Ingrese su tipo de sangre (A, B, AB, O): ").strip().upper()
if tipoSangre == "A":
    print("Puede donar a: A, AB. Puede recibir de: A, O.")
elif tipoSangre == "B":
    print("Puede donar a: B, AB. Puede recibir de: B, O.")
elif tipoSangre == "AB":
    print("Puede donar a: AB. Puede recibir de: A, B, AB, O.")
elif tipoSangre == "O":
    print("Puede donar a: A, B, AB, O. Puede recibir de: O.")
else:
    print("Tipo de sangre inválido.")