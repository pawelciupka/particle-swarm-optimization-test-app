import random
import math
from functions_factory import *
from pso.pso import Pso

if __name__ == "__PSO__":
    main()


def run_pso(function, num_particles, maxiter):
    # Granice układu [min,max]
    bounds = function.bounds
    Pso(func=function.func, num_dimensions=function.num_dimensions, bounds=bounds,
        num_particles=num_particles, maxiter=maxiter)


for func in functions:
    run_pso(func(), 50, 100)
