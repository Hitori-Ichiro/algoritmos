letra1 = input("Ingrese la primera letra: ")
letra2 = input("Ingrese la segunda letra: ")
if letra1 == letra2:
    print("Las letras son iguales.")
elif letra1 > letra2:
    print(f"La letra '{letra1}' es mayor alfabéticamente que '{letra2}'.")
else:
    print(f"La letra '{letra2}' es mayor alfabéticamente que '{letra1}'.")