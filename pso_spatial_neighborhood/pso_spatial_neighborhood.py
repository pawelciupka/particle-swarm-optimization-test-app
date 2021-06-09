from pso_parent.pso_parent import PsoParent
from math import *


class PsoSpatialNeigh(PsoParent):
    def __init__(self, func, num_dimensions, bounds, num_particles, maxiter):
        # Liczba iteracji
        self.maxiter = maxiter

        super(PsoSpatialNeigh, self).__init__("PSO - Spatial Neighborhood", func,
                                              num_dimensions, bounds, num_particles)

    def update_velocity_and_position(self, iter):
        # Zaktualizuj prędkość i pozycję wszystkich cząsteczek w roju
        #
        # Maksymalna odległość pomiędzy cząsteczkami w roju
        max_distance = self.get_max_distance_between_particles()
        # Wartość progowa dla aktualnej iteracji
        threshold = self.calculate_floating_threshold_value(iter)

        for i in range(0, self.num_particles):
            neighborhoods_pos_best = list(self.swarm[i].position)
            neighborhoods_value_best = self.swarm[i].value

            # Przeszukaj wszystkich sąsiadów
            for j in range(0, self.num_particles):
                if i == j:
                    continue

                # Sprawdź, czy wartość parametru sąsiedztwa dwóch cząstek jest mniejsza niż wartość progowa
                if self.calculate_neighborhood_parameter(max_distance, self.swarm[i], self.swarm[j]) < threshold:
                    # Sprawdź czy wartość cząsteczki jest mniejsza niż najmniejsza wartość cząsteczki sąsiadów
                    if self.swarm[j].value < neighborhoods_value_best:
                        neighborhoods_pos_best = list(self.swarm[j].position)
                        neighborhoods_value_best = self.swarm[j].value

            self.swarm[i].update_velocity(neighborhoods_pos_best, iter)
            self.swarm[i].update_position(self.bounds)

    def calculate_distance(self, particle1, particle2):
        # Oblicz odległość pomiędzy cząsteczkami
        #
        return dist(list(particle1.position), list(particle2.position))

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
        if max_distance != 0:
            return self.calculate_distance(particle1, particle2) / max_distance
        return 0

    def calculate_floating_threshold_value(self, iter):
        # Oblicz zmienną wartość progową sąsiedztwa
        #
        return (3*iter + 0.6*self.maxiter) / self.maxiter
