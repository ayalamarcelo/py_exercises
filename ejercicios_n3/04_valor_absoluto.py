# 4. Crear una función que, dado un número, devuelva su valor absoluto. El valor 
# absoluto de un número es el mismo número sin considerar el signo. 

def valor_absoluto(numero):
    if numero >= 0:
        print(f"Su valor absoluto es: {numero}")
    else:
        print(f"Su valor absoluto es: {numero * -1}")

valor_absoluto(-12)