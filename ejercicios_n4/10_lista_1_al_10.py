# 10. Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra 
# lista esos números elevados al cuadrado. 

uno_al_diez = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nros_elevados = []

for numero in uno_al_diez:
    res = numero * numero
    nros_elevados.append(res)

print(f"Lista con números elevados al cuadrado: {nros_elevados}")    