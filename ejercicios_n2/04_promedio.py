entero = None
acc = 0
total = 0

for i in range(5):
    entero = float(input("Ingrese un numero entero: "))
    total += entero
    acc += 1

promedio = float(total / acc)
print(f"El promedio de tus enteros ingresados es: {promedio}")