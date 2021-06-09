import json
import pandas as pd


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
