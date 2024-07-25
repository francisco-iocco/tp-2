from math import factorial
cantEstudiante = 4

def bonus2():
    posiciones = (cantEstudiante*cantEstudiante)-cantEstudiante
    numerador = factorial(posiciones)
    denominador = factorial(2) * factorial((posiciones-2))
    posibleMatcheo = numerador // denominador
    return posibleMatcheo

print(bonus2())

