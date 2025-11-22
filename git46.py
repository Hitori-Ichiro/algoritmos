contrasena = input("Ingrese una contraseña: ")
if (any(c.islower() for c in contrasena) and
    any(c.isupper() for c in contrasena) and
    any(c.isdigit() for c in contrasena) and
    len(contrasena) >= 8):
    print("Contraseña válida.")
else:
    print("Contraseña inválida. Debe contener al menos una mayúscula, una minúscula, un número y tener al menos 8 caracteres.")