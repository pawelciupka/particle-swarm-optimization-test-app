from math import *
from os import truncate
from helper import *

config = load_configuration()
maxiter = config["maxiter"]


# - Wektor musi składać się z 3 współczynników:
# w  - współczynnik inercyjny
# c1 - współczynnik kognitywyny
# c2 - współczynnik socjalny
# - Każdy współczynnik jest funkcją!
# - Każda funkcja musi zawierać taki sam zestaw parametrów

def get_coefficients_vector(particle, iter):
    # coeff_vector = w_1(particle, iter), c1_1(particle, iter), c2_1(particle, iter)
    # coeff_vector = w_2(particle, iter), c1_2(particle, iter), c2_2(particle, iter)
    # coeff_vector = w_3(particle, iter), c1_3(particle, iter), c2_3(particle, iter)
    # coeff_vector = w_4(particle, iter), c1_4(particle, iter), c2_4(particle, iter)
    coeff_vector = w_5(particle, iter), c1_5(particle, iter), c2_5(particle, iter)
    return coeff_vector

# Grupa pierwsza - START
def w_1(particle, iter):
    return 0.6
def c1_1(particle, iter):
    return 1.7
def c2_1(particle, iter):
    return 1.7
# Grupa pierwsza - STOP


## Grupa druga - START
def w_2(particle, iter):
    return 0.729
def c1_2(particle, iter):
    return 1.494
def c2_2(particle, iter):
    return 1.494
## Grupa druga - STOP


### Grupa trzecia - START
def w_3(particle, iter):
    return linear_by_iteration(iter, 0.9, 0.4)
def c1_3(particle, iter):
    return linear_by_iteration(iter, 2.75, 0.5)
def c2_3(particle, iter):
    return linear_by_iteration(iter, 0.5, 2.75)
### Grupa trzecia - STOP


#### Grupa czwarta - START
def w_4(particle, iter):
    return linear_by_iteration(iter, 0.9, 0.4)
def c1_4(particle, iter):
    return linear_by_iteration(iter, 2.5, 0.5)
def c2_4(particle, iter):
    return linear_by_iteration(iter, 0.5, 2.5)
#### Grupa czwarta - STOP


##### Grupa piąta - START
def w_5(particle, iter):
    return 0.8
def c1_5(particle, iter):
    return 1.1
def c2_5(particle, iter):
    return 1.8
##### Grupa piąta - STOP




# Funkcje pomocnicze
def linear_by_iteration(iter, initial_value, final_value):
    return (initial_value - final_value) * ((maxiter - iter) / maxiter) + final_value
