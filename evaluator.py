import numpy as np
import datetime


class Evaluator:
    def __init__(self, func, maxiter, num_runs, algorithm):
        # Funkcja
        self.func = func
        # Algorytm domyślny
        self.algorithm_default = algorithm
        # Algorytm
        self.algorithm = algorithm
        # Maksymalna liczba iteracji
        self.maxiter = maxiter
        # Liczba uruchomień algorytmu
        self.num_runs = num_runs
        # Liczba uruchomień algorytmu, w których znaleziono rozwiązanie
        self.num_successful_runs = 0
        # Iteracje, w których znaleziono rozwiązanie
        self.successful_runs_iters = []
        # Przewidywane najlepsze rozwiązania
        self.predictions = []
        # Znalezione najlepsze rozwiązania
        self.best_solutions = []
        # Znalezione najgorsze rozwiązania
        self.worst_solutions = []
        # Czasy działania algorytmów
        self.durations = []
        # Najlepsze wartości algorytmu dla poszczególnych iteracji
        self.best_solutions_per_iteration = []
            
        self.result_precision = 3

        for i in range(0, self.num_runs):
            self.predictions.append(self.func.solution)

        self.main()

    def stop_condition(self, iter):
        # Warunek stopu
        # 1. Jeżeli liczba iteracji zostanie przekroczona
        # 2. Jeżeli zostanie znalezione rozwiązanie
        #
        if iter < self.maxiter:
            if self.algorithm.g_value_best != None:
                if self.algorithm.g_value_best <= self.func.solution+self.func.accuracy and self.algorithm.g_value_best >= self.func.solution-self.func.accuracy:
                    # Zwiększ liczbe pomyślnie zakończonych testów
                    self.num_successful_runs += 1
                    # Dodaj liczbe iteracji do listy z liczbą iteracji pomyślnie zakończonych testów
                    self.successful_runs_iters.append(iter)
                    # Dodaj najlepsze rozwiązanie do listy najlepszych rozwiązań
                    self.best_solutions.append(
                        round(self.algorithm.g_value_best, self.result_precision))
                    # Dodaj najgorsze rozwiązanie do listy najgorszych rozwiązań
                    self.worst_solutions.append(
                        round(self.algorithm.g_value_worst, self.result_precision))
                    return False
            return True
        else:
            # Dodaj najlepsze rozwiązanie do listy najlepszych rozwiązań
            self.best_solutions.append(
                round(self.algorithm.g_value_best, self.result_precision))
            # Dodaj najgorsze rozwiązanie do listy najgorszych rozwiązań
            self.worst_solutions.append(
                round(self.algorithm.g_value_worst, self.result_precision))
            return False

    def main(self):
        # Główna pętla
        #
        for run in range(0, self.num_runs):
            # Zresetuj algorytm przed ponownym uruchomieniem testu
            iter = 0
            self.algorithm.reset()
            self.algorithm.init_swarm()

            self.best_solutions_per_iteration.append([])

            # Rozpocznij pomiar czasu
            start = datetime.datetime.now()

            while self.stop_condition(iter):
                self.algorithm.main(iter)
                self.best_solutions_per_iteration[run].append(self.algorithm.g_value_best)
                iter += 1

            # Zakończ pomiar czasu
            self.durations.append(datetime.datetime.now() - start)

    def efficiency(self):
        # Skuteczność = liczba pomyślnie zakończonych uruchomień / liczba uruchomień
        #
        return round(self.num_successful_runs / self.num_runs, self.result_precision)

    def avg_successful_iters(self):
        # Średnia liczba iteracji w pomyślnie zakończonych uruchomieniach
        #
        if self.successful_runs_iters != []:
            sum_iters = 0
            for iters in self.successful_runs_iters:
                sum_iters += iters
            return round(sum_iters / len(self.successful_runs_iters), self.result_precision)
        else:
            return 0

    def avg_best_solutions(self):
        # Średnia wartość najlepszych osobników
        #
        return round(np.array(self.best_solutions).mean(), self.result_precision)

    def best_solution(self):
        # Najlepsza wartość osobnika
        #
        return sorted(self.best_solutions)[0]

    def worst_solution(self):
        # Najgorsza wartość osobnika
        #
        return sorted(self.worst_solutions, reverse=True)[0]

    def std(self):
        # Odchylenie standardowe
        #
        return round(np.std(self.best_solutions), self.result_precision)

    def median(self):
        # Mediana
        #
        return round(np.median(self.best_solutions), self.result_precision)

    def avg_duration(self):
        # Średni czas działania algorytmu
        #
        return round(np.array(self.durations).mean().total_seconds(), self.result_precision)

    def mse(self):
        # Mean Squared Error
        #
        actual, pred = np.array(
            self.best_solutions), np.array(self.predictions)
        return round(np.square(np.subtract(actual, pred)).mean(), self.result_precision)

    def rmse(self):
        # Root mean squared error
        #
        actual, pred = np.array(
            self.best_solutions), np.array(self.predictions)
        return round(np.sqrt(np.square(np.subtract(actual, pred)).mean()), self.result_precision)

    def results(self):
        # Zbierz wszystkie rezultaty, które mają być wyeksportowane do excela
        #
        return [self.efficiency(), self.avg_successful_iters(), self.avg_best_solutions(), self.best_solution(), self.worst_solution(), self.std(), self.median(), self.avg_duration()]

    def avg_best_solutions_per_iteration(self):
        # Zbierz średnie wartości najlepszych rozwiązań dla wszystkich uruchomień algorytmu
        #
        result = []
        # Zsumuj najlepszą wartość cząsteczki w roju w każdej iteracji ze wszystkich uruchomień algorytmu 
        for iteration in range(0, self.maxiter):
            iteration_sum = 0
            for run in self.best_solutions_per_iteration:
                try:
                    iteration_sum += run[iteration]
                except:
                    iteration_sum += run[-1]
                
            # Podziel obliczoną sumę przez ilość uruchomień
            result.append(round(iteration_sum/self.num_runs, self.result_precision))
        return result
