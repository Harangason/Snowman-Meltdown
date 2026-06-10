import json
import os

def get_snowman_meltdown():
    # TODO: Build your game loop here.
    # JSON-Datei öffnen und laden
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Verbindet den Ordner sauber mit dem Dateinamen
        json_path = os.path.join(script_dir, "snowman.json")
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if "snowman" not in data:
            print("No snowman found in the JSON file.")
            return
        if not isinstance(data["snowman"], list):
            print("snowman is not a list.")
        else:
            print("snowman is a list.")
        return data["snowman"]
    except FileNotFoundError:
        print(("snowman.json not found."))

    # Den Schneemann aus der Liste Zeile für Zeile ausgeben
