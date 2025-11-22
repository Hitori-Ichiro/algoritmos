usuario_correcto = "angel"
contrasena_correcta = "troya"
usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")
if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")
    