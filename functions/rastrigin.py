from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/rastr.html
def rastrigin():
    f = Function()
    f.name = "RASTRIGIN"
    f.solution = 0
    f.solution_position = [0, 0]
    f.num_dimensions = 30           # get only if config nun_dimensions is equal to 0
    f.bounds = [-5.12, 5.12]
    f.accuracy = 30
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
