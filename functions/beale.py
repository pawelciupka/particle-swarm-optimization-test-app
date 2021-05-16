from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/beale.html
def beale():
    f = Function()
    f.name = "BEALE"
    f.solution = 0
    f.solution_position = [3, 0.5]
    f.num_dimensions = 2
    f.bounds = [-4.5, 4.5]
    f.func = f_beale
    # f.print_solution()
    return f


def f_beale(position):
    x1, x2 = position
    return (1.5 - x1 + x1*x2)**2 + (2.25 - x1 + x1*x2**2)**2 + (2.625 - x1 + x1*x2**3)**2
