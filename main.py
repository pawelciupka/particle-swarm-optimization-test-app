from plot_result import PlotResult
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
        config = load_configuration(True)
        self.num_dimensions = config['num_dimensions']
        self.num_particles = config["num_particles"]
        self.maxiter = config["maxiter"]
        self.num_runs = config["num_runs"]
        self.num_neighborhoods = config["num_neighborhoods"]
        self.num_tournament_particles = config["num_tournament_particles"]
        self.results = []
        self.avg_best_solutions_per_iteration = []

    def main(self):
        # Główny punkt aplikacji
        #
        # Wykonaj dla wszystkich wybranych algorytmów

        for algorithm in self.algorithms():
            for func in self.functions():
                # Wykonaj ewaluacje
                algorithm_obj = algorithm(func())
                eval = Evaluator(func(), self.maxiter,
                                 self.num_runs, algorithm_obj)

                # Dodaj wyniki do excela
                self.add_to_export_results(
                    func().name, algorithm_obj.name, eval.results())

                # Dodaj listę średnich rozwiązać per iteracja
                plot_result = PlotResult(
                    algorithm_obj, func(), eval.avg_best_solutions_per_iteration())
                self.avg_best_solutions_per_iteration.append(plot_result)

        # Wyeksportuj wyniki do excela
        export_results(self.results)

        # Wyświetl wykresy z wynikami
        # plot_results_per_algorithm(
        #     self.uniques_algorithms(), self.avg_best_solutions_per_iteration)
        plot_results_per_function(
            self.uniques_functions(), self.avg_best_solutions_per_iteration)

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
        return Pso(func=function.func, num_dimensions=get_num_dimensions(self.num_dimensions, function.num_dimensions), bounds=function.bounds,
                   num_particles=self.num_particles)

    def pso_ring_topology(self, function):
        # Algorytm PSO z modyfikacją sąsiedztwa według indeksu - topologia pierścienia
        #
        return PsoRingTplgy(func=function.func, num_dimensions=get_num_dimensions(self.num_dimensions, function.num_dimensions), bounds=function.bounds,
                            num_particles=self.num_particles, num_neighborhoods=self.num_neighborhoods)

    def pso_spatial_neighborhood(self, function):
        # Algorytm PSO z modyfikacją sąsiedztwa przestrzennego z progiem zmiennym w procesie iteracji
        #
        return PsoSpatialNeigh(func=function.func, num_dimensions=get_num_dimensions(self.num_dimensions, function.num_dimensions), bounds=function.bounds,
                               num_particles=self.num_particles, maxiter=self.maxiter)

    def pso_star_topology(self, function):
        # Algorytm PSO z modyfikacją sąsiedztwa - topologia gwiazdy
        #
        return PsoStarTplgy(func=function.func, num_dimensions=get_num_dimensions(self.num_dimensions, function.num_dimensions), bounds=function.bounds,
                            num_particles=self.num_particles)

    def pso_selection(self, function):
        # Algorytm PSO z modyfikacją ewolucyjną - selekcja
        #
        return PsoSelection(func=function.func, num_dimensions=get_num_dimensions(self.num_dimensions, function.num_dimensions), bounds=function.bounds,
                            num_particles=self.num_particles, num_tournament_particles=self.num_tournament_particles)

    ###
    # Metody, służące do wybrania testowanych algorytmów, funkcji
    ###

    def algorithms(self):
        # Wybierz algorytmy, które zostaną przetestowane
        #
        algorithms = []
        # algorithms.append(self.pso)
        # algorithms.append(self.pso_ring_topology)
        algorithms.append(self.pso_spatial_neighborhood)
        # algorithms.append(self.pso_star_topology)
        # algorithms.append(self.pso_selection)
        return algorithms

    def uniques_algorithms(self):
        res = []
        func = self.uniques_functions()[0]
        for algorithm in self.algorithms():
            algorithm_obj = algorithm(func)
            res.append(algorithm_obj)
        return res

    def functions(self):
        # Wybierz funkcje celu, które zostaną przetestowane
        #
        functions = []
        # functions.append(sphere)
        # functions.append(f2)
        # functions.append(rosenbrock)
        # functions.append(griewank)
        # functions.append(rastrigin)
        functions.append(ackley)
        # functions.append(schwefel)
        # functions.append(zakharov)
        return functions

    def uniques_functions(self):
        res = []
        for function in self.functions():
            res.append(function())
        return res


main = Main()
main.main()
