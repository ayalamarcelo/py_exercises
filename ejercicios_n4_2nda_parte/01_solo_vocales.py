# 1. Hacer una función que reciba un string y que imprima solamente los 
# caracteres que sean vocales.

def imprimir_vocales():
    texto = input("Ingrese un texto: ")
    vocales = "aáÁAeéÉEiíÍIoóÓOúÚU"

    for caracter in texto:
        if caracter in vocales:
            print(caracter, end="")
    print()

imprimir_vocales()