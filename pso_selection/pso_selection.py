import random
from pso_selection.pso_selection_particle import PsoSelectionParticle


class PsoSelection():
    def __init__(self, func, num_dimensions, bounds, num_particles, num_tournament_particles):
        # Nazwa
        self.name = "PSO - Selection"
        # Funkcja celu
        self.func = func
        # Liczba wymiarów
        self.num_dimensions = num_dimensions
        # Graniczne wartości cząstek
        self.bounds = bounds
        # Liczba cząsteczek
        self.num_particles = num_particles
        # Liczba cząsteczek, biorąca udział w turnieju
        self.num_tournament_particles = num_tournament_particles
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
            self.swarm.append(PsoSelectionParticle(initial_pos))
            self.swarm[i].evaluate(self.func)

    def main(self, iter):
        # Główna pętla
        #
        for j in range(0, self.num_particles):
            self.swarm[j].evaluate(self.func)

            self.tournament_selection(self.swarm[j], j)

            # Sprawdź, czy aktualna cząsteczka jest najlepsza
            if self.g_value_best == None or self.swarm[j].value < self.g_value_best:
                self.g_pos_best = list(self.swarm[j].position)
                self.g_value_best = float(self.swarm[j].value)

        self.assign_positions_of_better_half()
        self.update_velocity_and_position(iter)

    def tournament_selection(self, particle, current_particle_index):
        # Selekcja turniejowa
        #
        # Wyzeruj liczbę punktów
        particle.reset_points()
        for i in range(0, self.num_tournament_particles):
            # Wylosuj indeks inny niż aktualnej cząsteczki
            index = random.randint(0, self.num_particles-1)
            while current_particle_index == index:
                index = random.randint(0, self.num_particles-1)

            # Sprawdź, czy wartość aktualnej cząsteczki jest większa od cząsteczki turniejowej
            if particle.value > self.swarm[index].value:
                particle.add_point()

    def assign_positions_of_better_half(self):
        # Posortuj rój na podstawie liczby punktów (od największego do najmniejszego)
        # Przypisz położenia lepszej połowy roju do cząsteczek z gorszej połowy
        #
        self.swarm = sorted(self.swarm, key=sort_by_points, reverse=True)
        half_swarm = int(self.num_particles/2)
        for i in range(0, half_swarm):
            self.swarm[i+half_swarm].position = self.swarm[i].position

    def update_velocity_and_position(self, iter):
        # Aktualizacja prędkości i pozycji wszystkich cząsteczek w roju
        #
        for i in range(0, self.num_particles):
            self.swarm[i].update_velocity(self.g_pos_best, iter)
            self.swarm[i].update_position(self.bounds)


def sort_by_points(k):
    return k.points
