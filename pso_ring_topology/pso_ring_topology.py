from pso_parent.pso_parent import PsoParent


class PsoRingTplgy(PsoParent):
    def __init__(self, func, num_dimensions, bounds, num_particles, num_neighborhoods):
        # Liczba (parzysta) sąsiadujących cząsteczek
        self.num_neighborhoods = num_neighborhoods

        super(PsoRingTplgy, self).__init__("PSO - Ring Topology",
                                           func, num_dimensions, bounds, num_particles)

    def update_velocity_and_position(self, iter):
        # Zaktualizuj prędkość i pozycję wszystkich cząsteczek w roju
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
