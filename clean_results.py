import os, os.path

print("Czyszczenie plików wynikowych.")
counter = 0

results_path = "./results"
for root, dirs, files in os.walk(results_path):
    for file in files:
        if ".xlsx" in file or ".png" in file:
            print(os.path.join(root, file))
            counter += 1
            os.remove(os.path.join(root, file))

print("\nUsunięto " + str(counter) + " plików.")