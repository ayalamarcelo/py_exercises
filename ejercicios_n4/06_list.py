# 6. Hacer una lista con 5 nombres, y realizar las siguientes actividades 
# con la misma: 
# a. Cambiar el último elemento de la lista y cambiar el último nombre 
# por “Juan”. Olvidándonos de que sabemos que tiene 5 elementos, 
# ¿Cómo podría saber cuál es el último elemento si no sé la longitud? 
# b. Devolver el nombre que esté a dos posiciones del final. 
# ¿Cómo hacemos para que nos funcione para cualquier lista y no solo 
# para la que tenga 5 elementos?  
# c. Recorrer la lista e imprimir cada nombre por pantalla.  
# d. Imprimir por pantalla la lista con 3 repeticiones, usar el operador 
# repetición (*). 

def separador():
    print("")
    print("=====================SEPARDOR=========================")
    print("")

nombres = ["sol", "lara", "maria", "yael", "carolina"]
print(nombres[-1])
print(nombres[-3])
nombres.append("juan")
print(nombres)

separador()

for n in nombres:
    print(n, end=", ")

separador()

print(nombres * 3)