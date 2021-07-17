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
    f.accuracy = 30
    f.func = f_rosenbrock
    # f.print_solution()
    return f


def f_rosenbrock(position):
    d = len(position)
    sum = 0

    for ii in range(1, d):
        xi = position[ii]    #x i+1
        xii = position[ii-1] #x i
        sum += 100*((xi**2)-xii)**2+(1-xi)**2
    
    return sum