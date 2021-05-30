from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/rastr.html
# num_dimension = 1,...,d
def rastrigin():
    f = Function()
    f.name = "RASTRIGIN"
    f.solution = 0
    f.solution_position = [0, 0]
    f.num_dimensions = 5
    f.bounds = [-5.12, 5.12]
    f.func = f_rastrigin
    # f.print_solution()
    return f


def f_rastrigin(position):
    d = len(position)
    sum = 0

    for ii in range(0, d):
        xi = position[ii]
        sum = sum + (xi**2 - 10*cos(2*pi*xi))

    return 10*d + sum
