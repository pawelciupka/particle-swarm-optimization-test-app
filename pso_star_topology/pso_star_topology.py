import random
from pso_star_topology.pso_star_topology_particle import PsoStarTplgyParticle


class PsoStarTplgy():
    def __init__(self, func, num_dimensions, bounds, num_particles, maxiter):
        # Funkcja celu
        self.func = func
        # Liczba wymiarów
        self.num_dimensions = num_dimensions
        # Graniczne wartości cząstek
        self.bounds = bounds
        # Liczba cząsteczek
        self.num_particles = num_particles
        # Liczba iteracji
        self.maxiter = maxiter
        # Najlepsza pozycja roju
        self.g_pos_best = []
        # Wartość funkcji dopasowania w najlepszej pozycji roju
        self.g_value_best = None
        # Rój
        self.swarm = []
        # Indeks cząsteczki, która jest sąsiadem wszystkich cząsteczek w roju
        self.global_neighborhood_index = None

        # Ciało algorytmu
        self.init_swarm()
        self.main()
        self.print_solution()

    def init_swarm(self):
        # Inicjalizacja roju
        #
        for i in range(0, self.num_particles):
            initial_pos = []
            for j in range(0, self.num_dimensions):
                initial_pos.append(random.uniform(
                    self.bounds[0], self.bounds[1]))
            self.swarm.append(PsoStarTplgyParticle(initial_pos, i))

        self.global_neighborhood_index = random.randint(0, self.num_particles)

    def main(self):
        # Główna pętla
        #
        i = 0
        while i < self.maxiter:
            # Przejdź przez wszystkie cząsteczki w roju i je przelicz
            for j in range(0, self.num_particles):
                self.swarm[j].evaluate(self.func)

                # Sprawdź, czy aktualna cząsteczka jest najlepsza
                if self.g_value_best == None or self.swarm[j].value < self.g_value_best:
                    self.g_pos_best = list(self.swarm[j].position)
                    self.g_value_best = float(self.swarm[j].value)

            self.update_velocity_and_position()

            i += 1

    def update_velocity_and_position(self):
        # Przejdź przez wszystkie cząsteczki w roju i zaktualizuj prędkości i pozycje
        #
        global_neighborhood_pos = list(
            self.swarm[self.global_neighborhood_index].position)

        for i in range(0, self.num_particles):
            self.swarm[i].update_velocity(global_neighborhood_pos)
            self.swarm[i].update_position(self.bounds)

    def print_solution(self):
        # Wyświetl wyniki
        #
        print("Wyniki - Topologia gwiazdy")
        print("  Najlepsze rozwiązanie: ", self.g_value_best)
        print("  Najlepsza pozycja: ", self.g_pos_best)