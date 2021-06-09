from pso_parent.pso_parent import PsoParent
import random


class PsoSelection(PsoParent):
    def __init__(self, func, num_dimensions, bounds, num_particles, num_tournament_particles):
        # Liczba cząsteczek turniejowych
        self.num_tournament_particles = num_tournament_particles

        super(PsoSelection, self).__init__("PSO - Selection",
                                           func, num_dimensions, bounds, num_particles)

    def main(self, iter):
        # Główna pętla
        #
        for j in range(0, self.num_particles):
            self.swarm[j].evaluate(self.func)

            # Sprawdź, czy wartość aktualnej cząsteczki jest lepsza niż najlepsza znaleziona wartość
            if self.g_value_best == None or self.swarm[j].value < self.g_value_best:
                self.g_pos_best = list(self.swarm[j].position)
                self.g_value_best = float(self.swarm[j].value)
            # Sprawdź, czy wartość aktualnej cząsteczki jest gorsza niż najgorsza znaleziona wartość
            if self.g_value_worst == None or self.swarm[j].value > self.g_value_worst:
                self.g_pos_worst = list(self.swarm[j].position)
                self.g_value_worst = float(self.swarm[j].value)

            if iter > 0:
                self.tournament_selection(self.swarm[j], j)

        if iter > 0:
            self.assign_positions_of_better_half()

        self.update_velocity_and_position(iter)

    def tournament_selection(self, particle, current_particle_index):
        # Przeprowadź selekcję turniejową
        #
        # Wyzeruj liczbę punktów
        particle.reset_points()

        for i in range(0, self.num_tournament_particles):
            # Wylosuj indeks inny niż aktualnej cząsteczki
            index = random.randint(0, self.num_particles-1)
            while current_particle_index == index:
                index = random.randint(0, self.num_particles-1)

            # Sprawdź, czy wartość aktualnej cząsteczki jest lepsza od wartości cząsteczki turniejowej
            if particle.value < self.swarm[index].value:
                particle.add_point()

    def assign_positions_of_better_half(self):
        # Posortuj rój na podstawie liczby punktów (od największego do najmniejszego)
        # Przypisz położenia lepszej połowy roju do cząsteczek z gorszej połowy
        #
        self.swarm = sorted(self.swarm, key=sort_by_points, reverse=True)
        half_swarm = int(self.num_particles/2)
        for i in range(0, half_swarm):
            self.swarm[i+half_swarm].position = self.swarm[i].position


def sort_by_points(k):
    return k.points
