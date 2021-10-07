""" 
    "Problema del ebrio"
    nombre: Luis David Sanchez Paz 
    cedula:26.388.923
"""
from random import randint

repeticiones_experimento = randint(1, 10000)
experimento_exitoso = 0
experimento_fallido = 0

for iterator in range(repeticiones_experimento):
    """ 
    Punto de referencia de la posicion del ebrio
    utilizando ejes del plano cartesiano
     """
    eje_x = 0
    eje_y = 0

    for iterador in range(10):
        caminata = randint(1, 100)

        if caminata < 25:
            # Norte
            eje_y = eje_y + 1
        elif caminata < 50:
            # Sur
            eje_y = eje_y - 1
        elif caminata < 75:
            # Este
            eje_x = eje_x + 1
        else:
            # Oeste
            eje_x = eje_x - 1
    
    if eje_y == 2 or eje_y == -2 and eje_x == 0:
        experimento_exitoso = experimento_exitoso + 1
    elif eje_x == 2 or eje_x == -2 and eje_y == 0:
        experimento_exitoso = experimento_exitoso + 1
    elif eje_y == 1 or eje_y == -1 and eje_x == 1 or eje_x == -1:
        experimento_exitoso = experimento_exitoso + 1
    else:
        experimento_fallido = experimento_fallido + 1

resultado = experimento_exitoso / repeticiones_experimento
redondear_resultado = round(resultado, 6) * 100
aproximar_resultado = round(redondear_resultado, 5)

print(f"\nEl experimento se realizo: {repeticiones_experimento} veces")
print(f"pruebas exitosas: {experimento_exitoso}")
print(f"pruebas fallidas: {experimento_fallido}")
print(f"El ebrio, tiene una probabilidad de quedar a 2 calles de su inicio de: {aproximar_resultado}%")
