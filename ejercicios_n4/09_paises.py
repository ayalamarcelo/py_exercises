# 9. Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, 
# Alemania, Perú. 
# a.  Crear una tupla para cada país que contenga su nombre, su capital y el continente 
# donde se encuentra.  
# b. Guardar las tuplas en una lista.  
# c. Hacer una función que reciba por parámetros la lista, e imprima la información de 
# cada país con el siguiente formato: 
# País: <nombre>  
# Capital: <capital> 
# Continente: <continente> 
# Por ejemplo:  
# País: Japón 
# Capital: Tokio  
# Continente: Asia

pais1 = ("Francia", "Paris", "Europa")
pais2 = ("Argentina", "Buenos Aires", "Sudamerica")
pais3 = ("Japón", "Tokyo", "Asia")
pais4 = ("Alemania", "Berlin", "Europa")
pais5 = ("Perú", "Lima", "Sudamerica")

paises = [pais1, pais2, pais3, pais4, pais5]

def info_pais(paises):
    for nombre, capital, continente in paises:
        print(f"País: {nombre}")
        print(f"Capital: {capital}")
        print(f"Continente: {continente}")
        print("---------------------------")

info_pais(paises)

