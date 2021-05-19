from functions.function import Function
from math import *


#
def griewank():
    f = Function()
    f.name = "GRIEWANK"
    f.solution = 0
    f.solution_position = [0, 0]
    f.num_dimensions = 2
    f.bounds = [-600, 600]
    f.func = f_griewank
    # f.print_solution()
    return f


def f_griewank(position):
    d = len(position)
    sum = 0
    prod = 1

    for ii in range(1, d):
        xi = position[ii]
        sum = sum + xi**2/4000
        prod = prod * cos(xi/sqrt(ii))

    return sum - prod + 1
