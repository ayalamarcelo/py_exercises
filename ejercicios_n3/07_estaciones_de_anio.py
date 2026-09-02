"""
07. Se tienen letras para representar la estaciones del año:

* V para verano
* O para otoño
* I para invierno
* P para primavera

Crear una función que, dada una letra, imprima por pantalla la estación del año que representa
(es decir, si se ingresa V se mostrará por pantalla el mensaje "Verano").
En caso de no representar a ninguna estación mostrar un mensaje que diga "Error".
Probar la función creada llamándola con A, P, O, V e I.
"""

def estacion_del_anio():
    print("> Bienvenido/a, ingresa una letra para comenzar!")
    print("> V, O, I, P")
    estacion = input("_ ").upper()

    match estacion:
        case "V":
            print("Verano")
        case "O":
            print("Otoño")
        case "I":
            print("Invierno")
        case "P":
            print("Primavera")
        case _:
            print("Error!, intenta con las opciones recomendadas.")

estacion_del_anio()
