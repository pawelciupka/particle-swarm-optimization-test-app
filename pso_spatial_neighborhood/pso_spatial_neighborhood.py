import random
import math
from pso_spatial_neighborhood.pso_spatial_neighborhood_particle import PsoSpatialNeighParticle


class PsoSpatialNeigh():
    def __init__(self, func, num_dimensions, bounds, num_particles, maxiter):
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
            self.swarm.append(PsoSpatialNeighParticle(initial_pos))

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

            self.update_velocity_and_position(i)

            i += 1

    def update_velocity_and_position(self, iter):
        # Przejdź przez wszystkie cząsteczki w roju i zaktualizuj prędkości i pozycje
        #
        # Maksymalna odległość pomiędzy cząsteczkami w roju
        max_distance = self.get_max_distance_between_particles()
        # Wartość progowa dla aktualnej iteracji
        threshold = self.calculate_floating_threshold_value(iter)

        for i in range(0, self.num_particles):
            neighborhoods_pos_best = list(self.swarm[i].position)
            neighborhoods_value_best = self.swarm[i].value
            # Przejdź przez wszystkie inne cząsteczki w roju w poszukiwaniu sąsiadów
            for j in range(0, self.num_particles):
                if i == j:
                    continue

                # Sprawdź, czy wartość parametru sąsiedztwa dwóch cząstek jest mniejsza niż wartość progowa
                if self.calculate_neighborhood_parameter(max_distance, self.swarm[i], self.swarm[j]) < threshold:
                    # Sprawdź czy wartość cząsteczki jest mniejsza niż najmniejsza wartość cząsteczki sąsiadów
                    if self.swarm[j].value < neighborhoods_value_best:
                        neighborhoods_pos_best = list(self.swarm[j].position)

            self.swarm[i].update_velocity(neighborhoods_pos_best)
            self.swarm[i].update_position(self.bounds)

    def calculate_distance(self, particle1, particle2):
        # Oblicz odległość pomiędzy cząsteczkami
        #
        return math.dist(list(particle1.position), list(particle2.position))

    def get_max_distance_between_particles(self):
        # Znajdź maksymalną odległość pomiędzy cząsteczkami w roju
        #
        max_distance = 0
        for i in range(0, self.num_particles):
            for j in range(i+1, self.num_particles):
                distance = self.calculate_distance(
                    self.swarm[i], self.swarm[j])
                if distance > max_distance:
                    max_distance = distance
        return max_distance

    def calculate_neighborhood_parameter(self, max_distance, particle1, particle2):
        # Oblicz parametr sąsiedztwa
        #
        return self.calculate_distance(particle1, particle2) / max_distance

    def calculate_floating_threshold_value(self, iter):
        # Oblicz zmienną wartość progową sąsiedztwa
        #
        return (3*iter + 0.6*self.maxiter) / self.maxiter

    def print_solution(self):
        # Wyświetl wyniki
        #
        print("Wyniki - Sąsiedztwo Przestrzenne")
        print("  Najlepsze rozwiązanie: ", self.g_value_best)
        print("  Najlepsza pozycja: ", self.g_pos_best)
