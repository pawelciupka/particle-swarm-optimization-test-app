from functions_factory import *
from helper import *
from pso.pso import Pso
from pso_ring_topology.pso_ring_topology import PsoRingTplgy
from pso_spatial_neighborhood.pso_spatial_neighborhood import PsoSpatialNeigh
from pso_star_topology.pso_star_topology import PsoStarTplgy
from pso_selection.pso_selection import PsoSelection


# Klasyczny algorytm PSO
def run_pso(function, num_particles, maxiter):
    bounds = function.bounds
    Pso(func=function.func, num_dimensions=function.num_dimensions, bounds=bounds,
        num_particles=num_particles, maxiter=maxiter)


# Algorytm PSO z modyfikacją sąsiedztwa według indeksu - topologia pierścienia
def run_pso_ring_topology(function, num_particles, maxiter, num_neighborhoods):
    bounds = function.bounds
    PsoRingTplgy(func=function.func, num_dimensions=function.num_dimensions, bounds=bounds,
                 num_particles=num_particles, maxiter=maxiter, num_neighborhoods=num_neighborhoods)


# Algorytm PSO z modyfikacją sąsiedztwa przestrzennego z progiem zmiennym w procesie iteracji
def run_pso_spatial_neighborhood(function, num_particles, maxiter):
    bounds = function.bounds
    PsoSpatialNeigh(func=function.func, num_dimensions=function.num_dimensions, bounds=bounds,
                    num_particles=num_particles, maxiter=maxiter)


# Algorytm PSO z modyfikacją sąsiedztwa - topologia gwiazdy
def run_pso_star_topology(function, num_particles, maxiter):
    bounds = function.bounds
    PsoStarTplgy(func=function.func, num_dimensions=function.num_dimensions, bounds=bounds,
                 num_particles=num_particles, maxiter=maxiter)


# Algorytm PSO z modyfikacją ewolucyjną - selekcja
def run_pso_selection(function, num_particles, maxiter, num_tournament_particles):
    bounds = function.bounds
    PsoSelection(func=function.func, num_dimensions=function.num_dimensions, bounds=bounds,
                 num_particles=num_particles, maxiter=maxiter, num_tournament_particles=num_tournament_particles)


# Main
def main():
    config = load_configuration()
    for func in functions:
        # run_pso(
        #     func(), config["num_particles"], config["maxiter"])

        # run_pso_ring_topology(
        #     func(), config["num_particles"], config["maxiter"], config["num_neighborhoods"])

        # run_pso_spatial_neighborhood(
        #     func(), config["num_particles"], config["maxiter"])

        # run_pso_star_topology(
        #     func(), config["num_particles"], config["maxiter"])

        run_pso_selection(
            func(), config["num_particles"], config["maxiter"], config["num_tournament_particles"])


main()
