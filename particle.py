import random

class Particle:
    def __init__(self, initial_pos):        
        self.num_dimensions = len(initial_pos)

        self.position = []              # Pozycja cząsteczki
        self.value = -1                 # Wartość funkcji dopasowania cząsteczki
        self.velocity = []              # Prędkość cząsteczki
        self.p_pos_best = []            # Najlepsza pozycja cząsteczki
        self.p_value_best = -1          # Wartość funkcji dopasowania w najlepszej pozycji cząsteczki

        for i in range(0, self.num_dimensions):
            self.velocity.append(random.uniform(-1, 1))
            self.position.append(initial_pos[i])

    # Oblicz nową wartość i zaktualizuj najlepszą pozycję
    def evaluate(self, func):
        self.value = func(self.position)

        if self.value < self.p_value_best or self.p_value_best == -1:
            self.p_pos_best = self.position
            self.p_value_best = self.value

    # Zaktualizuj prędkość cząsteczki
    def update_velocity(self, pos_best_g):
        w = 0.5       # Współczynnik poprzedniej prędkości
        c1 = 1        # Współczynnik kognitywny
        c2 = 2        # Współczynnik socjalny

        for i in range(0, self.num_dimensions):
            r1 = random.random()
            r2 = random.random()

            vel_cognitive = c1 * r1 * (self.p_pos_best[i] - self.position[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + vel_cognitive + vel_social

    # Zaktualizuj pozycję cząsteczki
    def update_position(self, bounds):
        for i in range(0, self.num_dimensions):
            self.position[i] = self.position[i] + self.velocity[i]

            # Wyreguluj maksymalne położenie
            if self.position[i] > bounds[i][1]:
                self.position[i] = bounds[i][1]

            # Wyreguluj minimalne położenie
            if self.position[i] < bounds[i][0]:
                self.position[i] = bounds[i][0]
                