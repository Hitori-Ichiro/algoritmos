edad = int(input("Ingrese su edad: "))
if edad < 21:
    print("No puede alquilar un auto.")
elif 21 <= edad <= 25:
    print("Puede alquilar un auto. Se aplicará un cargo adicional del 15%.")
else:
    print("Puede alquilar un auto. No se aplicará ningún cargo adicional.")

        