categoria = input("Ingrese la categoría del cliente (A, B, C): ").upper()
montoCompra = float(input("Ingrese el monto de la compra: "))
if categoria == 'A':
    descuento = montoCompra * 0.30
elif categoria == 'B': 
    descuento = montoCompra * 0.20
elif categoria == 'C':
    descuento = montoCompra * 0.10
else:
    descuento = 0
montoFinal = montoCompra - descuento
print(f"El monto final después del descuento es: ${montoFinal:.2f}")