from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/schwef.html
# num_dimension = 1,...,d
def schwefel():
    f = Function()
    f.name = "SCHWEFEL"
    f.solution = 0
    f.solution_position = [420.9687, 420.9687]
    f.num_dimensions = 5
    f.bounds = [-500, 500]
    f.func = f_schwefel
    # f.print_solution()
    return f


def f_schwefel(position):
    d = len(position)
    sum = 0

    for ii in range(0, d):
        xi = position[ii]
        sum = sum + xi*sin(sqrt(abs(xi)))

    return 418.9829*d - sum
