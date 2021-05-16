import json
import pandas as pd


def load_configuration():
    # Wczytaj parametry konfiguracyjne
    #
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
    for key, value in config.items():
        print(key, ":", value)
    print("\n")
    return config


def export_results(results, filename="results.xlsx"):
    # Eksportuj rezultaty do excela
    #
    df = pd.DataFrame(results, columns=[
                      "Metoda", "Funkcja", "Skuteczność", "Średnia liczba iteracji"])
    df.to_excel(excel_writer="./results/"+filename)
