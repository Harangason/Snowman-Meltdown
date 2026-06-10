import random
import json
import os
# List of secret words


WORDS = ["python", "git", "github", "snowman", "meltdown"]

new_underscores = ""

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def snowman_meltdown():
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
    return data["snowman"]

def get_guess():
    # Eingabe vom Spieler holen
    while True:
        guess = input("\nGuess a letter: ").strip().lower()

        # Validierung: Eingabe darf nicht leer sein und sollte nur 1 Buchstabe sein
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Ungültige Eingabe. Bitte gib genau einen Buchstaben ein.")
            continue
        else:
            break
    return guess

def game_struct(secret_word, snowman_lines, max_fehler, fehler_counter, underscores):
    # 3. Die Hauptschleife(Game Loop)
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

        # Prüfen, ob der Schneemann komplett geschmolzen ist
        if fehler_counter >= max_fehler:
            print(f"\nGame Over! Der Schneemann ist geschmolzen. Das Wort war: {secret_word}")
            break

        guess = get_guess()

        # Prüfen, ob der Buchstabe im Wort ist
        if guess in secret_word.lower():
            print(f"Richtig! '{guess}' ist im Wort.")
            # ALLE Vorkommen des Buchstabens aufdecken (KEIN break!)
            for index, char in enumerate(secret_word.lower()):
                if char == guess:
                    underscores[index] = secret_word[index]  # Behält Groß-/Kleinschreibung des Originals bei

        else:
            print(f"Falsch! '{guess}' ist nicht im Wort.")
            fehler_counter += 1  # Schneemann schmilzt um eine Zeile
    return

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
    snowman_lines = snowman_meltdown()
    max_fehler = len(snowman_lines)  # Anzahl der Zeilen bestimmt die maximalen Fehlversuche
    fehler_counter = 0  # Wie viele Teile des Schneemanns schon geschmolzen sind
    reduse_counter = 1

    # Bleibt strikt eine Liste für die Zuweisung über den Index!
    underscores = ['_'] * len(secret_word)
    game_struct(secret_word, snowman_lines, max_fehler, fehler_counter, underscores)

if __name__ == "__main__":
    play_game()



