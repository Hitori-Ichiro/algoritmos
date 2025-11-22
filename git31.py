edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("No puede votar.")
elif 18 <= edad <= 70:
    print("Puede votar y es obligatorio.")
else:
    print("Puede votar, pero no es obligatorio.")