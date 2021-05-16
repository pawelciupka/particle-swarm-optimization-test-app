import random
from pso.pso_particle import PsoParticle


class PsoStarTplgy():
    def __init__(self, func, num_dimensions, bounds, num_particles):
        # Nazwa
        self.name = "PSO - Star"
        # Funkcja celu
        self.func = func
        # Liczba wymiarów
        self.num_dimensions = num_dimensions
        # Graniczne wartości cząstek
        self.bounds = bounds
        # Liczba cząsteczek
        self.num_particles = num_particles
        # Najlepsza pozycja roju
        self.g_pos_best = []
        # Wartość funkcji celu w najlepszej pozycji roju
        self.g_value_best = None
        # Rój
        self.swarm = []
        # Indeks cząsteczki, która jest sąsiadem wszystkich cząsteczek w roju
        self.global_neighborhood_index = None

    def reset(self):
        # Reset wartości algorytmu
        #
        self.g_pos_best = []
        self.g_value_best = None
        self.swarm = []

    def init_swarm(self):
        # Inicjalizacja roju
        #
        for i in range(0, self.num_particles):
            initial_pos = []
            for j in range(0, self.num_dimensions):
                initial_pos.append(random.uniform(
                    self.bounds[0], self.bounds[1]))
            self.swarm.append(PsoParticle(initial_pos))

        self.global_neighborhood_index = random.randint(
            0, self.num_particles-1)

    def main(self, iter):
        # Główna pętla
        #
        for j in range(0, self.num_particles):
            self.swarm[j].evaluate(self.func)

            # Sprawdź, czy aktualna cząsteczka jest najlepsza
            if self.g_value_best == None or self.swarm[j].value < self.g_value_best:
                self.g_pos_best = list(self.swarm[j].position)
                self.g_value_best = float(self.swarm[j].value)

        self.update_velocity_and_position(iter)

    def update_velocity_and_position(self, iter):
        # Aktualizacja prędkości i pozycji wszystkich cząsteczek w roju
        #
        global_neighborhood_pos = list(
            self.swarm[self.global_neighborhood_index].position)

        # Zaktualizuj prędkość i pozycję globalnego sąsiada korzystając z najlepszego znalezionego rozwiązania
        self.swarm[self.global_neighborhood_index].update_velocity(self.g_pos_best, iter)
        self.swarm[self.global_neighborhood_index].update_position(self.bounds)

        for i in range(0, self.num_particles):
            if i != self.global_neighborhood_index:
                self.swarm[i].update_velocity(global_neighborhood_pos, iter)
                self.swarm[i].update_position(self.bounds)
