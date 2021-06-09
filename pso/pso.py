from pso_parent.pso_parent import PsoParent


class Pso(PsoParent):
    def __init__(self, func, num_dimensions, bounds, num_particles):
        super(Pso, self).__init__("PSO", func,
                                  num_dimensions, bounds, num_particles)
