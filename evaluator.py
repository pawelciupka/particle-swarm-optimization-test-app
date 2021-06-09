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
                # Zwiększ liczbe pomyślnie zakończonych testów
                self.num_successful_runs += 1
                # Dodaj liczbe iteracji do listy z liczbą iteracji pomyślnie zakończonych testów
                self.successful_runs_iters.append(iter)
                # Dodaj najlepsze rozwiązanie do listy najlepszych rozwiązań
                self.best_solutions.append(
                    round(self.algorithm.g_value_best, self.stop_precision))
                # Dodaj najgorsze rozwiązanie do listy najgorszych rozwiązań
                self.worst_solutions.append(
                    round(self.algorithm.g_value_worst, self.stop_precision))
                return False
            else:
                return True
        else:
            # Dodaj najlepsze rozwiązanie do listy najlepszych rozwiązań
            self.best_solutions.append(
                round(self.algorithm.g_value_best, self.stop_precision))
            # Dodaj najgorsze rozwiązanie do listy najgorszych rozwiązań
            self.worst_solutions.append(
                round(self.algorithm.g_value_worst, self.stop_precision))
            return False

    def main(self):
        # Główna pętla
        #
        for run in range(0, self.num_runs):
            # Zresetuj algorytm przed ponownym uruchomieniem testu
            iter = 0
            self.algorithm.reset()
            self.algorithm.init_swarm()

            # Rozpocznij pomiar czasu
            start = datetime.datetime.now()

            while self.stop_condition(iter):
                self.algorithm.main(iter)
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

    def print_results(self):
        # Wyświetl wyniki
        #
        print("Algorytm: ", self.algorithm.name)
        print("Funkcja:  ", self.func.name)
        print("  Skuteczność:                  ", self.efficiency())
        print("  Średnia liczba iteracji       ", self.avg_successful_iters())
        print("  Średnia najlepszych wartości  ", self.avg_best_solutions())
        print("  Najlepsza znaleziona wartość  ", self.best_solution())
        print("  Najgorsza znaleziona wartość  ", self.worst_solution())
        print("  Odchylenie standardowe        ", self.std())
        print("  Mediana                       ", self.median())
        print("  Średni czas wykonywania [sec] ", self.avg_duration())
        print()

    @staticmethod
    def print_short_results_header():
        # Wyświetl nagłówek krótkich wyników
        #
        print("Algorytm | Funkcja | Skuteczność | Avg Iters | Avg Best | Best | Std | Median | Avg Time")

    def print_short_results(self):
        # Wyświetl krótkie wyniki
        #
        print(
            self.algorithm.name + ' | ' + 
            self.func.name + ' | ' + 
            str(self.efficiency()) + ' | ' + 
            str(self.avg_successful_iters()) + ' | ' +
            str(self.avg_best_solutions()) + ' | ' + 
            str(self.best_solution()) + ' | ' + 
            str(self.std()) + ' | ' + 
            str(self.median()) + ' | ' + 
            str(self.avg_duration()))
