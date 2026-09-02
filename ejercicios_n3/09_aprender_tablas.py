""" 
9. Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio 
anterior. Ahora se necesita una funcionalidad que permita a los niños aprender las 
tablas. Crear una función que reciba un número entero e imprima por pantalla la 
tabla de ese número del 1 al 10.  
"""

def aprender_tablas(numero):
    for i in range(10):
        print(numero * (i+1))

num = int(input("Ingresa un numero:_"))
aprender_tablas(num)

