from functions_factory import *
from helper import *
from evaluator import Evaluator
from pso.pso import Pso
from pso_ring_topology.pso_ring_topology import PsoRingTplgy
from pso_spatial_neighborhood.pso_spatial_neighborhood import PsoSpatialNeigh
from pso_star_topology.pso_star_topology import PsoStarTplgy
from pso_selection.pso_selection import PsoSelection


class Main:
    def __init__(self, ):
        config = load_configuration()

        self.num_particles = config["num_particles"]
        self.maxiter = config["maxiter"]
        self.num_runs = config["num_runs"]
        self.num_neighborhoods = config["num_neighborhoods"]
        self.num_tournament_particles = config["num_tournament_particles"]
        self.results = []

    def main(self):
        # Główny punkt aplikacji
        #
        # Wykonaj dla wszystkich wybranych algorytmów
        Evaluator.print_short_results_header()

        for algorithm in self.algorithms():
            # Wykonaj dla wszystkich wybranych funkcji celu
            for func in self.functions():
                # Wykonaj ewaluacje
                algorithm_obj = algorithm(func())
                eval = Evaluator(func(), self.maxiter,
                                 self.num_runs, algorithm_obj)
                eval.print_short_results()
                # eval.print_results()

                # Dodaj wyniki do excela
                self.add_to_export_results(
                    func().name, algorithm_obj.name, eval.results())

        # Wyeksportuj wyniki do excela
        export_results(self.results)

    def add_to_export_results(self, func_name, algorithm_name, evaluation_results):
        # Dodaj wyniki do excela
        #
        result = [algorithm_name, func_name]
        for r in evaluation_results:
            result.append(r)
        self.results.append(result)



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



    ###
    # Metody, służące do wybrania testowanych algorytmów, funkcji
    ###

    def algorithms(self):
        # Wybierz algorytmy, które zostaną przetestowane
        #
        algorithms = []
        algorithms.append(self.pso)
        # algorithms.append(self.pso_ring_topology)
        # algorithms.append(self.pso_spatial_neighborhood)
        # algorithms.append(self.pso_star_topology)
        # algorithms.append(self.pso_selection)
        return algorithms

    def functions(self):
        # Wybierz funkcje celu, które zostaną przetestowane
        #
        functions = []
        # Many Local Minima
        functions.append(ackley)        # Wiele wymiarów
        functions.append(griewank)      # Wiele wymiarów
        # functions.append(crossit)     # Dwa wymiary
        # functions.append(levy13)      # Dwa wymiary
        functions.append(levy)          # Wiele wymiarów
        functions.append(rastrigin)     # Wiele wymiarów
        functions.append(schwefel)      # Wiele wymiarów
        # # Bowl-Shaped
        # functions.append(boha1)       # Dwa wymiary
        # # Plate-Shaped
        # functions.append(booth)       # Dwa wymiary
        # # Steep Ridges/Drops
        # functions.append(easom)       # Dwa wymiary
        # # Other
        # functions.append(beale)       # Dwa wymiary
        return functions


main = Main()
main.main()
