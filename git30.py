ingresoAnual = float(input("Ingrese su ingreso anual en dólares: "))
if ingresoAnual <= 10000000:
    impuesto = 0
elif 10000001 <= ingresoAnual <= 40000000:
    impuesto = ingresoAnual * 0.12
elif 40000001 <= ingresoAnual <= 80000000:
    impuesto = ingresoAnual * 0.16
else:
    impuesto = ingresoAnual * 0.19
print(f"El impuesto anual a pagar es: ${impuesto:.2f}")