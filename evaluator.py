import numpy as np


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
        self.actuals = []

        self.stop_precision = 4
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
            if self.algorithm.g_value_best != None and round(self.func.solution, self.stop_precision) == round(self.algorithm.g_value_best, self.stop_precision):
                self.num_successful_runs += 1
                self.successful_runs_iters.append(iter)
                self.actuals.append(
                    round(self.algorithm.g_value_best, self.stop_precision))
                return False
            else:
                return True
        else:
            self.actuals.append(
                round(self.algorithm.g_value_best, self.stop_precision))
            return False

    def main(self):
        # Główna pętla
        #
        for run in range(0, self.num_runs):
            # Reset przed ponownym uruchomieniem
            iter = 0
            self.algorithm.reset()
            self.algorithm.init_swarm()

            while self.stop_condition(iter):
                self.algorithm.main(iter)
                iter += 1

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

    def mse(self):
        # Mean Squared Error
        #
        actual, pred = np.array(self.actuals), np.array(self.predictions)
        return round(np.square(np.subtract(actual, pred)).mean(), self.result_precision)

    def rmse(self):
        # Root mean squared error
        #
        actual, pred = np.array(self.actuals), np.array(self.predictions)
        return round(np.sqrt(np.square(np.subtract(actual, pred)).mean()), self.result_precision)

    def results(self):
        # Rezultaty
        #
        return [self.efficiency(), self.avg_successful_iters(), self.mse(), self.rmse()]

    def print_results(self):
        # Wyświetlanie rezultatów
        #
        print("Algorytm: ", self.algorithm.name)
        print("Funkcja:  ", self.func.name)
        print("  Skuteczność: ", self.efficiency())
        print("  Średnia liczba potrzebnych iteracji ",
              self.avg_successful_iters())
        print("  MSE: ", self.mse())
        print("  RMSE: ", self.rmse())
        print()

    def print_short_results(self):
        # Wyświetlanie rezultatów
        #
        print(self.algorithm.name + ' | ' + self.func.name + ' | ' + str(self.efficiency()) +
              ' | ' + str(self.rmse()) + ' | ' + str(self.actuals))
