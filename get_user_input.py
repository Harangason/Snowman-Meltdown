def get_input_letter():
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