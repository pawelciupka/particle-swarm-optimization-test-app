from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/ackley.html
def ackley():
    f = Function()
    f.name = "ACKLEY FUNCTION"
    f.solution = 0
    f.solution_position = [0, 0]
    f.num_dimensions = 2
    f.bounds = [-32.768, 32.768]
    f.func = f_ackley
    f.print_solution()
    return f


def f_ackley(position, a=20, b=0.2, c=2*pi):
    d = len(position)

    sum1 = 0
    sum2 = 0
    for pos in position:
        sum1 = sum1 + pos**2
        sum2 = sum2 + cos(c*pos)

    term1 = -a * exp(-b*sqrt(sum1/d))
    term2 = -exp(sum2/d)

    return term1 + term2 + a + exp(1)
