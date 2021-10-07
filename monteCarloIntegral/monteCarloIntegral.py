from sympy import var, integrate
from numpy import random
""" 
    Proyecto: Resolviendo Integral definida por el Metodo Monte Carlo
    integrantes: 
        - Sanchez Paz, Luis David, cedula: 26.388.923
        - Lanchez, Brando, cedula: 25239611
"""
# Variables globales
lower_limit = 2
upper_limit = 3
variable_x = var('x')
sumatoria_de_iteraciones = 0

# Resolviendo la integral de forma analitica
definite_integral = integrate(3 * (x ** 2), (x, 2, 3))

#  Numero de interaciones proporcionado por el usuario
numero_iteraciones = int(input("Introduzca el numero de iteraciones para el experimento: "))

# Crear arreglo de numero aleatorios
arreglo_num_aleatorios = random.uniform(lower_limit, upper_limit, int(numero_iteraciones))

for iterator in range(numero_iteraciones):
    sumatoria_de_iteraciones += (3 * (iterator ** 2))

# Resultado aproximado de la integral definida
resultAprox_integral_definida = (lower_limit - upper_limit) * sumatoria_de_iteraciones / float(numero_iteraciones)

# Porcentaje de error por parte del resultado aproximado entre el resultado definitivo (real)
porcentaje_error = (abs(sumatoria_de_iteraciones - definite_integral) / definite_integral) * 100

print(f"Valor definitivo de la integral definida: {definite_integral}")
print(f"Valor aproximado de la integral definida: {resultAprox_integral_definida}")
print(f"El valor aproximado de: {resultAprox_integral_definida} tiene un porcentaje de error de {round(porcentaje_error, 3)}% con relacion al resultado definitivo (real) de la integral definida el cual su valor es: {definite_integral}")
