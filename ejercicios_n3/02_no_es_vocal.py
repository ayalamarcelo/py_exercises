# Repetir el punto anterior, pero con la expresión que determina que una letra NO es 
# vocal.

def es_una_vocal():
    letra = input("Ingrese una letra:_")
    if letra.lower() not in "aeiou":
        print(f"{letra} no es una vocal")
    else:
        print(f"{letra} es una vocal")

es_una_vocal()