class Function:
    name = None
    solution = None
    solution_position = None
    num_dimensions = None
    bounds = None
    func = None

    def print_solution(self):
        print("\n--------------------")
        print("Funkcja {0}".format(self.name))
        print("  Rozwiązanie: {0}".format(self.solution))
        print("  Pozycja: {0}".format(self.solution_position))
