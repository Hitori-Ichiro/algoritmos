sumaMultiplos = 0
for i in range(1, 101):
    if i % 5 == 0 or i % 7 == 0:
        sumaMultiplos += i
print(sumaMultiplos)