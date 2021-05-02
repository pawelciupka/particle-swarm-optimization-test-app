from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/easom.html
def easom():
    f = Function()
    f.name = "EASOM FUNCTION"
    f.solution = -1
    f.solution_position = [pi, pi]
    f.num_dimensions = 2
    f.bounds = [-100, 100]
    f.func = f_easom
    f.print_solution()
    return f


def f_easom(position):
    x1, x2 = position
    fact1 = -cos(x1)*cos(x2)
    fact2 = exp(-(x1-pi)**2-(x2-pi)**2)
    return fact1*fact2
