from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/levy.html
def levy():
    f = Function()
    f.name = "LEVY"
    f.solution = 0
    f.solution_position = [1, 1]
    f.num_dimensions = 30           # get only if config nun_dimensions is equal to 0
    f.bounds = [-10, 10]
    f.func = f_levy
    # f.print_solution()
    return f


def f_levy(position):
    d = len(position)

    term1 = (sin(pi*w(position, 0)))**2
    term3 = (w(position, d-1)-1)**2 * (1+(sin(2*pi*w(position, d-1)))**2)

    sum = 0

    for ii in range(0, d-1):
        wi = w(position, ii)
        new = (wi-1)**2 * (1+10*(sin(pi*wi+1))**2)
        sum = sum + new

    return term1 + sum + term3


def w(position, i):
    return 1 + (position[i] - 1)/4
