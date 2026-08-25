def es_par():
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        print(f"El numero: {numero} es par y")
        if numero < 10:
            print(f"El numero {numero} es menor a 10")
        else:
            print(f"El numero {numero} es mayor a 10")
    else:
        print(f"El numero: {numero} no es par")

es_par()