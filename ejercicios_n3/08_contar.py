""" 
Se quiere hacer un programa para enseñar a unos niños a contar. Crear una
función que reciba un número entero e imprima por pantalla los números 
del 1 hasta ese número con la estructura de control iterativa for.  
"""

def aprendiendo_a_contar(numero):
    for i in range(numero):
        print(i + 1, end=", ")

numero = int(input("Ingresa un numero:_"))
aprendiendo_a_contar(numero)