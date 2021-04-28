from particle import Particle

class PSO():
    def __init__(self, func, initial_pos, bounds, num_particles, maxiter):
        num_dimensions = len(initial_pos)

        g_pos_best = []                 # Najlepsza pozycja roju
        g_value_best = -1               # Wartość funkcji dopasowania w najlepszej pozycji roju

        # Inicjalizacja roju
        swarm = []
        for i in range(0, num_particles):
            swarm.append(Particle(initial_pos))

        # Główna pętla 
        i = 0
        while i < maxiter:
            #print(i,g_value_best)
            # Przejdź przez wszystkie cząsteczki w roju i je przelicz
            for j in range(0, num_particles):
                swarm[j].evaluate(func)

                # Sprawdź, czy aktualna cząsteczka jest najlepsza
                if swarm[j].value < g_value_best or g_value_best == -1:
                    g_pos_best = list(swarm[j].position)
                    g_value_best = float(swarm[j].value)

            # Przejdź przez wszystkie cząsteczki w roju i zaktualizuj prędkości i pozycje            
            for j in range(0, num_particles):
                swarm[j].update_velocity(g_pos_best)
                swarm[j].update_position(bounds)
            i += 1

        # Wyświetl wyniki
        print("Wyniki ")
        print("  Najlepsze rozwiązanie: ", g_value_best)
        print("  Najlepsza pozycja: ", g_pos_best)