from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/boha.html
def boha1():
    f = Function()
    f.name = "BOHACHEVSKY 1"
    f.solution = 0
    f.solution_position = [0, 0]
    f.num_dimensions = 2
    f.bounds = [-100, 100]
    f.func = f_boha1
    # f.print_solution()
    return f


def f_boha1(position):
    x1, x2 = position
    term1 = x1**2
    term2 = 2*x2**2
    term3 = -0.3 * cos(3*pi*x1)
    term4 = -0.4 * cos(4*pi*x2)

    return term1 + term2 + term3 + term4 + 0.7
