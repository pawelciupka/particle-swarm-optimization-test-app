from functions.function import Function
from math import *


#
def f2():
    f = Function()
    f.name = "F2"
    f.solution = 0
    f.solution_position = [0, 0]
    f.num_dimensions = 30           # get only if config nun_dimensions is equal to 0
    f.bounds = [-100, 100]
    f.accuracy = 4                  # 0.0001
    f.func = f_f2
    # f.print_solution()
    return f


def f_f2(position):
    d = len(position)
    sum = 0

    for ii in range (1, d+1):
        xi = position[ii-1]
        sum = sum + (xi-ii)**2

    return sum