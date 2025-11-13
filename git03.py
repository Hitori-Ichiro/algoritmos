edad = int(input("Ingrese su edad: "))  
if edad < 12:
    print("Eres un niño.")
elif 12 <= edad < 18:
    print("Eres un adolescente.")
elif 18 <= edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")