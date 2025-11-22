edad = int(input("Ingrese su edad: "))
if 0 <= edad <= 12:
    fase = "Infancia"
elif 13 <= edad <= 17:
    fase = "Adolescencia"
elif 18 <= edad <= 59:
    fase = "Adultez"
else:
    fase = "Vejez"
print(f"Usted está en la fase de vida: {fase}.")