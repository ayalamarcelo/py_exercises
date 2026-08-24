
def numero_vecino():
    numero_ingresado = int(input("Ingrese un numero:_"))
    ant = numero_ingresado + 1 
    sig = numero_ingresado - 1

    print(f"El numero anterior a: {numero_ingresado} es: {ant}")
    print(f"El numero siguiente a: {numero_ingresado} es: {sig}")

numero_vecino()


