horaCompra = int(input("Ingrese la hora de compra (formato 24 horas, solo la hora): "))
montoCompra = float(input("Ingrese el monto de la compra: "))
if horaCompra < 12:
    descuento = 0.10
    print("Se aplica un 10% de descuento.")
elif horaCompra >= 18:
    descuento = 0.20
    print("Se aplica un 20% de descuento.")
else:
    descuento = 0.0
    print("No se aplica descuento.")
totalPagar = montoCompra * (1 - descuento)
print(f"El total a pagar es: ${totalPagar:.2f}")