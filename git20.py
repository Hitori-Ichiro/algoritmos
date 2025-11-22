mes = int(input("Ingrese un mes (1-12): "))
if 1 <= mes <= 3:
    print("El mes pertenece al primer trimestre.")
elif 4 <= mes <= 6:
    print("El mes pertenece al segundo trimestre.")
elif 7 <= mes <= 9:
    print("El mes pertenece al tercer trimestre.")
elif 10 <= mes <= 12:
    print("El mes pertenece al cuarto trimestre.")
else:
    print("Número de mes inválido. Por favor ingrese un número entre 1 y 12.")