import random
import math
from functions_factory import *
from pso import PSO

if __name__ == "__PSO__":
    main()


def run_pso(function, num_particles, maxiter):
    # Położenie początkowe cząsteczek [x1,x2...]
    initial = function.initial
    # Granice układu [(x1_min,x1_max),(x2_min,x2_max)...]
    bounds = function.bounds
    PSO(func=function.func, initial_pos=initial, bounds=bounds,
        num_particles=num_particles, maxiter=maxiter)


for func in functions:
    run_pso(func(), 50, 100)
