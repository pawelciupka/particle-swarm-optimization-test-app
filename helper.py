import json
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os


def load_configuration(do_print=False):
    # Wczytaj parametry konfiguracyjne
    #
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
    if do_print:
        print("\n" + get_configuration_print(config) + "\n")
    return config


def get_configuration_print(config):
    # Zwróć jednolinijkowy tekst z wartościami konfiguracyjnymi
    #
    return "dim: " + str(config["num_dimensions"]) + " | parts: " + str(config["num_particles"]) + " | iters: " + str(config["maxiter"]) + " | neighs: " + str(config["num_neighborhoods"]) + " | tourns: " + str(config["num_tournament_particles"])


def get_configuration_file_string(config):
    # Zwróć krótki tekst z wartościami konfiguracyjnymi
    #
    result = ""
    for key, value in config.items():
        result += str(value) + "_"
    return result


def export_results(results, do_print=True):
    # Eksportuj rezultaty do excela
    #
    columns_en = ["Algorytm", "Funkcja", "Skuteczność", "Avg Iters",
                  "Avg Best", "Best", "Worst", "Std", "Median", "Avg Time"]
    df_en = pd.DataFrame(results, columns=columns_en)
    if do_print:
        print(df_en)

    columns_pl = ["Algorytm", "Funkcja", "Skuteczność", "Średnia liczba iteracji", "Średnia najlepszych wartości",
                  "Najlepsza znaleziona wartość", "Najgorsza znaleziona wartość", "Odchylenie standardowe", "Mediana", "Średni czas wykonywania [sec]"]
    df_pl = pd.DataFrame(results, columns=columns_pl)
    filename = get_now_sign_string() + "___" + get_configuration_file_string(load_configuration()) + "_"
    df_pl.to_excel(excel_writer="./results/"+filename+".xlsx")


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
        plt.savefig("./results/plots/" + get_now_sign_string() +
                    "_function_" + function.name)
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
        plt.savefig("./results/plots/Algorytm " + algorithm.name)
        if should_plot:
            plt.show()


def get_num_dimensions(config_value, function_value):
    # Zwróć liczbę wymiarów funkcji, w zależności od wartości konfiguracyjnej
    #
    if config_value == 0:
        return function_value
    return config_value


def get_now_sign_string():
    # Zwróć tekstowyznacznik aktualnego czasu
    #
    return datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
