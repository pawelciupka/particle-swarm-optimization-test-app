import json
from functions_factory import *
from pso.pso import Pso
from pso_ring_topology.pso_ring_topology import PsoRingTplgy


# Wczytaj parametry konfiguracyjne
def load_configuration():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
    for key, value in config.items():
        print(key, ":", value)
    print("\n")
    return config


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


# Main
def main():
    config = load_configuration()
    for func in functions:
        # run_pso(func(), config["num_particles"], config["maxiter"])
        run_pso_ring_topology(
            func(), config["num_particles"], config["maxiter"], config["num_neighborhoods"])


main()
