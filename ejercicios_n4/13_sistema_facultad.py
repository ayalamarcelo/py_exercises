# 13. Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las 
# materias que va haciendo. Para eso, crear una función que le pregunte al usuario la 
# materia que quiere almacenar, e ir guardando la información en una lista hasta que 
# ingrese una ‘X’. ¿Qué funciones de listas no permiten insertar en una lista?  

# def almacenar_materias():
#     lista_materia = []
#     while True:
#         materia = input("Ingrese la materia que quiere almacenar (o x para salir): ")
#         if materia.lower() == "x":
#             break
#         lista_materia.append(materia)
#     print(lista_materia)

def almacenar_materias():
    lista_materias = []
    materia = input("Ingrese la materia que quiere almacenar (o X para salir): ")

    while materia.lower() not in("x", "X"):
        lista_materias.append(materia)
        materia = input("Ingrese la materia que quiere almacenar (o x para salir): ")
    print(lista_materias)

almacenar_materias()