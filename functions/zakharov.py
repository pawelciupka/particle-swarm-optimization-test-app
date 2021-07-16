from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/zakharov.html
def zakharov():
    f = Function()
    f.name = "ZAKHAROV"
    f.solution = 0
    f.solution_position = [0, 0]
    f.num_dimensions = 30           # get only if config nun_dimensions is equal to 0
    f.bounds = [-10, 10]
    f.accuracy = 3                  # 0.001
    f.func = f_zakharov
    # f.print_solution()
    return f


def f_zakharov(position):
    d = len(position)
    sum1 = 0
    sum2 = 0

    for ii in range(1, d+1):
        xi = position[ii-1]
        sum1 = sum1 + xi**2
        sum2 = sum2 + 0.5*ii*xi
    
    return sum1 + sum2**2 + sum2**4