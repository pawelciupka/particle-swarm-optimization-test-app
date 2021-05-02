from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/bukin6.html
def bukin6():
    f = Function()
    f.name = "BUKIN FUNCTION N. 6"
    f.solution = 0
    f.solution_position = [-10, 1]
    f.num_dimensions = 2
    f.bounds = [-15, -5]
    f.func = f_bukin6
    f.print_solution()
    return f


def f_bukin6(position):
    x1, x2 = position
    term1 = 100 * sqrt(abs(x2 - 0.01*x1**2))
    term2 = 0.01 * abs(x1+10)
    return term1 + term2
