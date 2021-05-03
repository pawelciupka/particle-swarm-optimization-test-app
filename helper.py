import json


# Wczytaj parametry konfiguracyjne
def load_configuration():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
    for key, value in config.items():
        print(key, ":", value)
    print("\n")
    return config
