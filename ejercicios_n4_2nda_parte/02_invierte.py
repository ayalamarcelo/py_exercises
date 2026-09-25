# 2. Hacer una función que reciba un string y que lo invierta.

def invertir_string():
    string = input("Ingrese un texto: ")
    print(string)

    new_string = list(string)
    new_string = list(reversed(new_string))

    string = ''.join(new_string)
    print(string)



invertir_string()