from math import *


# - Wektor musi składać się z 3 współczynników
# - Każdy współczynnik jest funkcją!
# - Każda funkcja musi zawierać taki sam zestaw parametrów

def inertia_coefficient(iter=0):
    return 0.5


def cognitive_coefficient(iter=0):
    return 1.2


def social_coefficient(iter=0):
    return 4 - cognitive_coefficient(iter)
    if iter > 0:
        return log(iter)
    else:
        return 1
