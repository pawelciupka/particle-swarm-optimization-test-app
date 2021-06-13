class PlotResult:
    def __init__(self, algorithm, function, iterations_results):
        self.algorithm = algorithm
        self.function = function
        self.iterations_results = iterations_results

        self.function_name = function.name
        self.algorithm_name = algorithm.name
