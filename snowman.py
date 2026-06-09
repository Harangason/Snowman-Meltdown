import random
import json
import os
# List of secret words


WORDS = ["python", "git", "github", "snowman", "meltdown"]


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

    while True:
        try:
            # For now, simply prompt the user once:
            guess = input("Guess a letter: ").strip().lower()
            print("You guessed:", guess)
            if guess in secret_word.lower():
                lines_reduce = data["snowman"]
                i = 0
                max_length = len(lines_reduce)
                # Eine while-Schleife statt 'for', um die Zeilen nacheinander zu drucken
                while i < max_length - 1:
                    print(f"\n{data["snowman"][i]}")
                    i += 1
            else:
                print("Incorrect guess. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a single letter.")



if __name__ == "__main__":
    play_game()



