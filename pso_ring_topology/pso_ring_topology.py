import random
from pso.pso_particle import PsoParticle


class PsoRingTplgy():
    def __init__(self, func, num_dimensions, bounds, num_particles, num_neighborhoods):
        # Nazwa
        self.name = "PSO - Topologia pierścienia"
        # Funkcja celu
        self.func = func
        # Liczba wymiarów
        self.num_dimensions = num_dimensions
        # Graniczne wartości cząstek
        self.bounds = bounds
        # Liczba cząsteczek
        self.num_particles = num_particles
        # Liczba sąsiadów (wartość parzysta)
        self.num_neighborhoods = num_neighborhoods
        # Najlepsza pozycja roju
        self.g_pos_best = []
        # Wartość funkcji celu w najlepszej pozycji roju
        self.g_value_best = None
        # Rój
        self.swarm = []

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
        # Zaktualizuj prędkości i pozycje wszystkich cząsteczek w roju
        #
        for i in range(0, self.num_particles):
            neighborhoods_pos_best = self.swarm[i].position
            neighborhoods_value_best = self.swarm[i].value

            # Znajdź najlepsze położenie wśród sąsiadów
            for j in range(0, int(self.num_neighborhoods/2)):
                index1 = (i+j) % self.num_particles
                if self.swarm[index1].value < neighborhoods_value_best:
                    neighborhoods_pos_best = list(self.swarm[index1].position)

                index2 = (i-j) % self.num_particles
                if self.swarm[index2].value < neighborhoods_value_best:
                    neighborhoods_pos_best = list(self.swarm[index2].position)

            self.swarm[i].update_velocity(neighborhoods_pos_best, iter)
            self.swarm[i].update_position(self.bounds)
