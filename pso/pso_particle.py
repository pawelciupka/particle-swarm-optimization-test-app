import random
import coefficient_factory


class PsoParticle:
    def __init__(self, initial_pos):
        self.num_dimensions = len(initial_pos)

        # Pozycja cząsteczki
        self.position = []
        # Wartość funkcji celu cząsteczki
        self.value = None
        # Prędkość cząsteczki
        self.velocity = []
        # Najlepsza pozycja cząsteczki
        self.p_pos_best = []
        # Wartość funkcji celu w najlepszej pozycji cząsteczki
        self.p_value_best = None
        # Ilość punktów turniejowych
        self.points = 0

        for i in range(0, self.num_dimensions):
            self.velocity.append(random.uniform(-1, 1))
            self.position.append(initial_pos[i])

    def evaluate(self, func):
        # Oblicz nową wartość i zaktualizuj najlepszą pozycję
        #
        self.value = func(self.position)

        if self.p_value_best == None or self.value < self.p_value_best:
            self.p_pos_best = self.position
            self.p_value_best = self.value

    def update_velocity(self, pos_best_g, iter):
        # Zaktualizuj prędkość cząsteczki
        #
        # Współczynnik inercji/kognitywny/socjalny (w, c1, c2)
        w, c1, c2 = coefficient_factory.get_coefficients_vector(self, iter)

        for i in range(0, self.num_dimensions):
            r1 = random.random()
            r2 = random.random()

            vel_cognitive = c1 * r1 * (self.p_pos_best[i] - self.position[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + \
                vel_cognitive + vel_social

    def update_position(self, bounds):
        # Zaktualizuj pozycję cząsteczki
        #
        for i in range(0, self.num_dimensions):
            self.position[i] = self.position[i] + self.velocity[i]

            # Wyreguluj maksymalne położenie
            if self.position[i] > bounds[1]:
                self.position[i] = bounds[1]

            # Wyreguluj minimalne położenie
            if self.position[i] < bounds[0]:
                self.position[i] = bounds[0]

    def add_point(self):
        self.points += 1

    def reset_points(self):
        self.points = 0
