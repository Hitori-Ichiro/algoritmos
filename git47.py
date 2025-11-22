precio = float(input("Ingrese el precio del producto: "))
esencial = input("¿El producto es esencial? (si/no): ").strip().lower
if esencial == "si":
    iva = 0.04
else:
    iva = 0.21
precioFinal = precio * (1 + iva)
print(f"El precio final con IVA es: ${precioFinal:.2f}")

