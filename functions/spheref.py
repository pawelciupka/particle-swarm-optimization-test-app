from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/spheref.html
def spheref():
    f = Function()
    f.name = "SPHERE"
    f.solution = 0
    f.solution_position = [0, 0]
    f.num_dimensions = 2
    f.bounds = [-5.12, 5.12]
    f.func = f_spheref
    # f.print_solution()
    return f


def f_spheref(position):
    x1, x2 = position
    sum = x1**2 + x2**2

    return sum
