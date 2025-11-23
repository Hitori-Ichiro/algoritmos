totalCompra = float(input("Introduce el total de la compra: "))
if totalCompra > 100:
    descuento = totalCompra * 0.10
    totalConDescuento = totalCompra - descuento
    print(F"Tienes un descuento del 10%. Total a pagar: {totalConDescuento}")
else:
    print(f"No tienes descuento. Total a pagar: {totalCompra}")