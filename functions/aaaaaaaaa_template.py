from functions.function import Function
from math import *


# 
def function_template():
    f = Function()
    f.name = ""
    f.solution = sol
    f.solution_position = [solution_pos_min, solution_pos_max]
    f.initial = [initial_min, initial_max]
    f.bounds = bounds=[(bound_min, bound_max), (bound_min, bound_max)]
    f.func = f_name
    f.print_solution()
    return f

def f_name(position):
    x1, x2 = position
    return 1