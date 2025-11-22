edad1 = int(input("Ingrese la edad de la primera persona: "))
edad2 = int(input("Ingrese la edad de la segunda persona: "))
edad3 = int(input("Ingrese la edad de la tercera persona: "))
if edad1 >= edad2 and edad1 >= edad3:
    mayor = edad1
    if edad2 <= edad3:
        menor = edad2
    else:
        menor = edad3
elif edad2 >= edad1 and edad2 >= edad3:
    mayor = edad2
    if edad1 <= edad3:
        menor = edad1
    else:
        menor = edad3
else:
    mayor = edad3
    if edad1 <= edad2:
        menor = edad1
    else:
        menor = edad2
print(f"La edad mayor es: {mayor}")
print(f"La edad menor es: {menor}")