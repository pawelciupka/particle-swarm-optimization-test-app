import random
import math
import func_factory
from pso import PSO

if __name__ == "__PSO__":
    main()

initial=[5, 5]                      # Położenie początkowe cząsteczek [x1,x2...]
bounds=[(-10, 10), (-10, 10)]       # Granice układu [(x1_min,x1_max),(x2_min,x2_max)...]
PSO(func_factory.func1, initial, bounds, num_particles=15, maxiter=30)