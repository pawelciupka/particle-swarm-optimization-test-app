import json
import pandas as pd
import matplotlib.pyplot as plt


def load_configuration(do_print=False):
    # Wczytaj parametry konfiguracyjne
    #
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
    if do_print:
        for key, value in config.items():
            print(key, ":", value)
        print("\n")
    return config

def export_results(results, filename="results"):
    # Eksportuj rezultaty do excela
    #
    df = pd.DataFrame(results, columns=[
                      "Algorytm", "Funkcja", "Skuteczność", "Średnia liczba iteracji", "Średnia najlepszych wartości", "Najlepsza znaleziona wartość", "Najgorsza znaleziona wartość", "Odchylenie standardowe", "Mediana", "Średni czas wykonywania [sec]"])
    df.to_excel(excel_writer="./results/"+filename+".xlsx")


def plot_results_per_function(functions, results, should_plot=False):
    # Wyświetl wykresy z wynikami pogrupowanymi na funkcje
    #
    plt.xlabel("Numer iteracji")
    plt.ylabel("Wartość najlepszej cząsteczki")

    for function in functions:
        plt.clf()
        plt.title("Funkcja " + function.name)
        for res in results:
            if function.name == res.function_name:
                plt.plot(res.iterations_results, label=res.algorithm_name)
                plt.legend()
        plt.savefig("./results/plots/Funkcja "+ function.name)
        if should_plot:
            plt.show()


def plot_results_per_algorithm(algorithms, results, should_plot=False):
    # Wyświetl wykresy z wynikami pogrupowanymi na algorytmy
    #
    plt.xlabel("Numer iteracji")
    plt.ylabel("Wartość najlepszej cząsteczki")

    for algorithm in algorithms:
        plt.clf()
        plt.title("Algorytm " + algorithm.name)
        for res in results:
            if algorithm.name == res.algorithm_name:
                plt.plot(res.iterations_results, label=res.function_name)
                plt.legend()
        plt.savefig("./results/plots/Algorytm "+ algorithm.name)
        if should_plot:
            plt.show()

