import random
import json
import os
# List of secret words


WORDS = ["python", "git", "github", "snowman", "meltdown"]

new_underscores = ""

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

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

    except FileNotFoundError:
        print(("snowman.json not found."))

    # Den Schneemann aus der Liste Zeile für Zeile ausgeben
    for line in data["snowman"]:
        print(line)

    # 2. Spielvariablen initialisieren
    snowman_lines = data["snowman"]
    max_fehler = len(snowman_lines)  # Anzahl der Zeilen bestimmt die maximalen Fehlversuche
    fehler_counter = 0  # Wie viele Teile des Schneemanns schon geschmolzen sind
    reduse_counter = 1

    # Bleibt strikt eine Liste für die Zuweisung über den Index!
    underscores = ['_'] * len(secret_word)
    while True:
        # Aktuellen Zustand des Schneemanns zeichnen (schmilzt von unten nach oben)
        print("\n" + "=" * 30)
        aktuelle_zeilen = max_fehler - fehler_counter
        for i in range(aktuelle_zeilen):
            print(snowman_lines[i])

            # Aktuellen Wort-Fortschritt anzeigen (NUR beim Printen als String zusammenfügen)
            print("\nWort: " + " ".join(underscores))

            # Prüfen, ob das Spiel gewonnen wurde
            if "_" not in underscores:
                print("\nGlückwunsch! Du hast das Wort erraten und den Schneemann gerettet!")
                break

            max_length = len(lines_reduce)
            # Eine while-Schleife statt 'for', um die Zeilen nacheinander zu drucken
            while i < max_length - reduse_counter:
                print(f"{data["snowman"][i]}")
                i += 1
            for index, char in enumerate(secret_word):
                if char == guess:
                    underscores[index] = guess

            reduse_counter += 1
        else:
            print("Incorrect guess. Try again.")
            continue
        print(f"{underscores}")
        '''underscores += underscores.replace('_', guess, underscore_counter)
        #underscore = ' _ ' * (5 - underscore_counter)
        print(f"Word: {underscores}")
        underscore_counter += 1'''




if __name__ == "__main__":
    play_game()



