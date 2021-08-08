from pso_parent.pso_parent import PsoParent
import random
from pso.pso_particle import PsoParticle


class PsoStarTplgy(PsoParent):
    def __init__(self, func, num_dimensions, bounds, num_particles):
        # Indeks cząsteczki, która jest sąsiadem wszystkich cząsteczek w roju
        self.global_neighborhood_index = None

        super(PsoStarTplgy, self).__init__("PSO - Star Topology", func,
                                           num_dimensions, bounds, num_particles)

    def init_swarm(self):
        # Zainicjalizuj rój
        #
        for i in range(0, self.num_particles):
            initial_pos = []
            for j in range(0, self.num_dimensions):
                initial_pos.append(random.uniform(
                    self.bounds[0], self.bounds[1]))
            self.swarm.append(PsoParticle(initial_pos))

        self.global_neighborhood_index = random.randint(
            0, self.num_particles-1)

    def update_velocity_and_position(self, iter):
        # Zaktualizuj prędkość i pozycję wszystkich cząsteczek w roju
        #
        # Zaktualizuj prędkość i pozycję globalnego sąsiada korzystając z najlepszego znalezionego rozwiązania
        self.swarm[self.global_neighborhood_index].update_velocity(
            self.g_pos_best, iter)
        self.swarm[self.global_neighborhood_index].update_position(self.bounds)
        
        global_neighborhood_pos = list(
            self.swarm[self.global_neighborhood_index].position)

        for i in range(0, self.num_particles):
            if i != self.global_neighborhood_index:
                self.swarm[i].update_velocity(global_neighborhood_pos, iter)
                self.swarm[i].update_position(self.bounds)
