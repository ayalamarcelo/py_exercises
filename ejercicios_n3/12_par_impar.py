# 12. Escribir código que recorra los números del 1 al 20 y determine para cada uno si es 
# par o impar, imprimiendo un mensaje por pantalla en cada caso. Es decir, el output 
# esperado sería: 
# > El número 1 es impar. 
# > El número 2 es par. 
# … 
# > El número 20 es par. 


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for n in numbers:
    if n % 2 == 0:
        print(f"El número {n} es par")
    else:
        print(f"El numero {n} es impar") 