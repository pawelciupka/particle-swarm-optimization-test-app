from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/griewank.html
def griewank():
    f = Function()
    f.name = "GRIEWANK"
    f.solution = 0
    f.solution_position = [0, 0]
    f.num_dimensions = 30           # get only if config nun_dimensions is equal to 0
    f.bounds = [-600, 600]
    f.accuracy = 0.1
    f.func = f_griewank
    # f.print_solution()
    return f


def f_griewank(position):
    d = len(position)
    sum = 0
    prod = 1

    for ii in range(1, d+1):
        xi = position[ii-1]
        sum = sum + (xi**2)/4000
        prod = prod * cos(xi/sqrt(ii))

    return sum - prod + 1
