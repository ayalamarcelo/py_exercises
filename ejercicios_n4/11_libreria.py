# 11. Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en 
# una lista de la siguiente forma: [“El principito”, “It”, “Sherlock Holmes”...]. Se quiere 
# saber cuántos libros repetidos tienen. Hacer código que imprima para cada título, 
# cuántos ejemplares hay. 
# Aclaración: No se sabe la cantidad de elementos que tiene la lista, la lista nombrada es 
# solo un ejemplo. 

libros = ["El principito", "It", "Sherlock Holmes", "It", "Harry Potter", "It"]
contador = 0

for libro in libros:
    if libro == libro:
        contador = contador + 1
        print(f"El ejemplar {libro} se encuentra {contador} veces")
