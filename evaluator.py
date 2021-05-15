

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

        self.main()

    def stop_condition(self, iter):
        # Warunek stopu
        # 1. Jeżeli liczba iteracji zostanie przekroczona
        # 2. Jeżeli zostanie znalezione rozwiązanie
        #
        if iter < self.maxiter:
            if self.func.solution == self.algorithm.g_value_best:
                self.num_successful_runs += 1
                self.successful_runs_iters.append(iter)
                return False
            else:
                return True
        else:
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
        return self.num_successful_runs /  self.num_runs

    def avg_successful_iters(self):
        # Średnia liczba iteracji w pomyślnie zakończonych uruchomieniach
        #
        if self.successful_runs_iters != []:
            sum_iters = 0
            for iters in self.successful_runs_iters:
                sum_iters += iters
            return sum_iters / len(self.successful_runs_iters)
        else:
            return 0

    def results(self):
        # Rezultaty
        #
        print(self.algorithm.__class__)
        print("  Skuteczność: ", self.efficiency())
        print("  Średnia liczba potrzebnych iteracji ", self.avg_successful_iters())
        print()
