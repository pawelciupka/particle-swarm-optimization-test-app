from functions.function import Function
from math import *


# http://www.sfu.ca/~ssurjano/rosen.html
def rosenbrock():
    f = Function()
    f.name = "ROSENBROCK"
    f.solution = 0
    f.solution_position = [1, 1]
    f.num_dimensions = 30           # get only if config nun_dimensions is equal to 0
    f.bounds = [-2.048, 2.048]
    f.accuracy = 1/3                # 30
    f.func = f_rosenbrock
    # f.print_solution()
    return f


def f_rosenbrock(position):
    sum = 0

    for i in range(len(position)-1):
        sum += 100*((position[i]**2)-position[i+1])**2+(1-position[i])**2
    
    return sum