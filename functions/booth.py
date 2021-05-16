from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/booth.html
def booth():
    f = Function()
    f.name = "BOOTH FUNCTION"
    f.solution = 0
    f.solution_position = [1, 3]
    f.num_dimensions = 2
    f.bounds = [-10, 10]
    f.func = f_booth
    # f.print_solution()
    return f


def f_booth(position):
    x1, x2 = position
    term1 = (x1 + 2*x2 - 7)**2
    term2 = (2*x1 + x2 - 5)**2

    return term1 + term2
