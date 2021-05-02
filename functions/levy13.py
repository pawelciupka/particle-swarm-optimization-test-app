from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/levy13.html
def levy13():
    f = Function()
    f.name = "LEVY FUNCTION N. 13"
    f.solution = 0
    f.solution_position = [1, 1]
    f.num_dimensions = 2
    f.bounds = [-10, 10]
    f.func = f_levy13
    f.print_solution()
    return f


def f_levy13(position):
    x1, x2 = position
    term1 = (sin(3*pi*x1))**2
    term2 = (x1-1)**2 * (1+(sin(3*pi*x2))**2)
    term3 = (x2-1)**2 * (1+(sin(2*pi*x2))**2)
    return term1 + term2 + term3
