montoTransferencia = float(input("Ingrese el monto de la transferencia: "))
saldoDisponible = float(input("Ingrese el saldo disponible en la cuenta: "))
if montoTransferencia > saldoDisponible:
    print("Transacción fraudulenta detectada.")
else:
    print("Transacción autorizada.")