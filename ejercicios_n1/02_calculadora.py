num_1 = float(input("Ingrese un primer valor: "))
num_2 = float(input("Ingrese un segundo valor: "))

print("Seleccion el tipo de operacion a realizar: ")
print("1: suma")
print("2: resta")
print("3: multiplicacion")
print("4: division")

operacion = int(input("_"))

resultado = 0

if operacion == 1:
    resultado = num_1 + num_2
elif operacion == 2:
    resultado = num_1 - num_2
elif operacion == 3:
    resultado = num_1 * num_2
else:
    resultado = num_1 / num_2

print(f"El resultado de tu operacion es: {resultado}")
