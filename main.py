from functions_factory import *
from helper import *
from evaluator import Evaluator
from pso.pso import Pso
from pso_ring_topology.pso_ring_topology import PsoRingTplgy
from pso_spatial_neighborhood.pso_spatial_neighborhood import PsoSpatialNeigh
from pso_star_topology.pso_star_topology import PsoStarTplgy
from pso_selection.pso_selection import PsoSelection


class Main:
    def __init__(self, functions):
        config = load_configuration()
    
        self.num_particles = config["num_particles"]
        self.maxiter = config["maxiter"]
        self.num_runs = config["num_runs"]
        self.num_neighborhoods = config["num_neighborhoods"]
        self.num_tournament_particles = config["num_tournament_particles"]

        self.functions = functions

    def main(self):
        # Główny punkt aplikacji
        #
        for func in self.functions:
            for algorithm in self.algorithms():
                algorithm_obj = algorithm(func())
                eval = Evaluator(func(), self.maxiter, self.num_runs, algorithm_obj)
                eval.results()
        
    def pso(self, function):
        # Klasyczny algorytm PSO
        #
        return Pso(func=function.func, num_dimensions=function.num_dimensions, bounds=function.bounds,
            num_particles=self.num_particles)
            
    def pso_ring_topology(self, function):
        # Algorytm PSO z modyfikacją sąsiedztwa według indeksu - topologia pierścienia
        #
        return PsoRingTplgy(func=function.func, num_dimensions=function.num_dimensions, bounds=function.bounds,
            num_particles=self.num_particles, num_neighborhoods=self.num_neighborhoods)
    
    def pso_spatial_neighborhood(self, function):
        # Algorytm PSO z modyfikacją sąsiedztwa przestrzennego z progiem zmiennym w procesie iteracji
        #
        return PsoSpatialNeigh(func=function.func, num_dimensions=function.num_dimensions, bounds=function.bounds,
            num_particles=self.num_particles, maxiter=self.maxiter)
            
    def pso_star_topology(self, function):
        # Algorytm PSO z modyfikacją sąsiedztwa - topologia gwiazdy
        #
        return PsoStarTplgy(func=function.func, num_dimensions=function.num_dimensions, bounds=function.bounds,
            num_particles=self.num_particles)
            
    def pso_selection(self, function):
        # Algorytm PSO z modyfikacją ewolucyjną - selekcja
        #
        return PsoSelection(func=function.func, num_dimensions=function.num_dimensions, bounds=function.bounds,
            num_particles=self.num_particles, num_tournament_particles=self.num_tournament_particles)

    def algorithms(self):
        # Lista testowanych algorytmów
        #
        return [self.pso, self.pso_ring_topology, self.pso_spatial_neighborhood, self.pso_star_topology, self.pso_selection]


main = Main(functions)
main.main()