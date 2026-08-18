import secrets

WORDS = ["python", "hangman", "keyboard", "internship", "coding"]
MAX_WRONG = 6


def choose_word():
    return secrets.choice(WORDS)


def display_state(word, guessed_letters, wrong_count):
    display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\nWord: {display}")
    print(f"Wrong guesses: {wrong_count}/{MAX_WRONG}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")


def play():
    word = choose_word()
    guessed_letters = set()
    wrong_count = 0

    print("=== HANGMAN ===")
    print(f"Guess the word! You have {MAX_WRONG} wrong attempts allowed.\n")

    while wrong_count < MAX_WRONG:
        display_state(word, guessed_letters, wrong_count)

        if all(letter in guessed_letters for letter in word):
            print(f"\nYou won! The word was '{word}'.")
            return

        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_count += 1
            print(f"Wrong! '{guess}' is not in the word.")

    print(f"\nYou lost! The word was '{word}'.")


if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break