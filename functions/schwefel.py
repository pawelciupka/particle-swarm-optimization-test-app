from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/schwef.html
def schwefel():
    f = Function()
    f.name = "SCHWEFEL"
    f.solution = 0
    f.solution_position = [420.9687, 420.9687]
    f.num_dimensions = 30           # get only if config nun_dimensions is equal to 0
    f.bounds = [-500, 500]
    f.accuracy = 0.000001
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
