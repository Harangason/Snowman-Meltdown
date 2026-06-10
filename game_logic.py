import random
import get_user_input as get_guess
import ascii_art as snowman_meltdown


WORDS = ["python", "git", "github", "snowman", "meltdown"]

new_underscores = ""

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def game_struct(secret_word, snowman_lines):
    # 3. Die Hauptschleife(Game Loop)


    max_mistakes = len(snowman_lines)  # Anzahl der Zeilen bestimmt die maximalen Fehlversuche
    mistakes = 0  # Wie viele Teile des Schneemanns schon geschmolzen sind
    underscores = ['_'] * len(secret_word)
    while True:
        display_game_state(mistakes, max_mistakes, snowman_lines)

        # Aktuellen Wort-Fortschritt anzeigen (NUR beim Printen als String zusammenfügen)
        print("\nWort: " + " ".join(underscores))

        # Prüfen, ob das Spiel gewonnen wurde
        if check_win(underscores):
            print("\nGlückwunsch! Du hast das Wort erraten und den Schneemann gerettet!")
            break

        # Prüfen, ob der Schneemann komplett geschmolzen ist
        if check_game_over(mistakes, max_mistakes):
            input("Press Enter to continue...")
            print(f"\nGame Over! Der Schneemann ist geschmolzen. Das Wort war: {secret_word}")
            break

        guess = get_guess.get_input_letter()
        guess = guess.lower().strip()  # Sicherstellen, dass Leerzeichen und Großschreibung keine Rolle spielen

        # Prüfen, ob der Buchstabe im Wort ist
        if guess in secret_word.lower():
            print(f"Richtig! '{guess}' ist im Wort.")
            # ALLE Vorkommen des Buchstabens aufdecken (KEIN break!)
            for index, char in enumerate(secret_word.lower()):
                if char == guess:
                    underscores[index] = secret_word[index]  # Behält Groß-/Kleinschreibung des Originals bei
        else:
            print(f"Falsch! '{guess}' ist nicht im Wort.")
            mistakes += 1  # Schneemann schmilzt um eine Zeile
    return

def check_mistake(mistakes, max_mistakes):
    return mistakes < max_mistakes

def check_game_over(mistakes, max_mistakes):
    return mistakes >= max_mistakes

def check_win(underscores):
    return "_" not in underscores

def display_game_state(mistakes, max_mistakes, snowman_lines):
    # Aktuellen Zustand des Schneemanns zeichnen (schmilzt von unten nach oben)
    print("\n" + "=" * 30)
    aktuelle_zeilen = max_mistakes - mistakes
    for i in range(aktuelle_zeilen):
        print(snowman_lines[i])
    return

def play_game_again():
    return input("Do you want to play again? (y/n): ").lower().strip() == "y"

def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line


    # Bleibt strikt eine Liste für die Zuweisung über den Index!
    # 2. Spielvariablen initialisieren
    snowman_lines = snowman_meltdown.get_snowman_meltdown()

    for line in snowman_lines:
        print(line)

    game_struct(secret_word, snowman_lines)


if __name__ == "__main__":
    play_game()
