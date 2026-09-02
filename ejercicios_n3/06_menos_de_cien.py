""" 
6. Escribir código que, dado dos enteros, determine si la suma de ambos da menos 
que 100. Si la suma de ambos es menor a 100, calcular cuánto falta para llegar a 
100 y mostrar por pantalla un mensaje con ese valor. Si la suma es mayor a 100, 
mostrar un mensaje diciendo “Llega a 100”. 

Extra: ¿Cómo harían para que el programa quede generalizado para cualquier 
límite, a elección del usuario, y no solo para 100?  
"""

def menos_de_cien():
    num_1 = int(input("Ingresa un valor: "))
    num_2 = int(input("Ingresa otro valor: "))
    limite = int(input("Ingrese un valor limite: "))

    if num_1 + num_2 >= limite:
        print(f"Llega a {limite}")
    else:
        print(f"Para llegar a {limite} te falta: {limite - (num_1 + num_2)}")


menos_de_cien()