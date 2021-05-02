from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/crossit.html
def crossit():
    f = Function()
    f.name = "CROSS-IN-TRAY"
    f.solution = -2.06261
    f.solution_position = [(1.3491, -1.3491), (1.3491, 1.3491),
                           (-1.3491, 1.3491), (-1.3491, -1.3491)]
    f.num_dimensions = 2
    f.bounds = [-10, 10]
    f.func = f_crossit
    f.print_solution()
    return f


def f_crossit(position):
    x1, x2 = position
    fact1 = sin(x1)*sin(x2)
    fact2 = exp(abs(100 - sqrt(x1**2+x2**2)/pi))

    return -0.0001 * (abs(fact1*fact2)+1)**0.1
