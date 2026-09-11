# 8. Hacer una función que reciba dos strings: un string y un substring, esto quiere decir que 
# el primero contenga al segundo. Se pide que la función devuelva al string habiendo 
# eliminado el substring del mismo. 

def substring(str1, str2):
    return f"{str1} {str2}"


str1 = input("Ingrese un string:_")
str2 = input("Ingrese otro string:_")
res_str = substring(str1, str2)
print(res_str)