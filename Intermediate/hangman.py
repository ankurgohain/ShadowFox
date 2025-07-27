import random

# Hangman ASCII visuals for each stage
HANGMAN_PICS = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========='''
]

# Word list with hints
WORDS = [
    ("python", "A popular programming language."),
    ("giraffe", "A tall African animal with a long neck."),
    ("astronaut", "Travels to space."),
    ("hangman", "The game you’re playing now."),
    ("pyramid", "A triangular structure found in Egypt."),
    ("volcano", "Erupts with lava."),
]

def choose_word():
    return random.choice(WORDS)

def display_board(missed, correct, secret_word):
    print(HANGMAN_PICS[len(missed)])
    print("\nMissed letters:", " ".join(missed))
    display = [letter if letter in correct else '_' for letter in secret_word]
    print("Word: ", " ".join(display))

def play_game():
    word, hint = choose_word()
    word = word.lower()
    correct_guesses = []
    missed_guesses = []

    print("\nWelcome to Hangman!")
    print(f"Hint: {hint}")

    while True:
        display_board(missed_guesses, correct_guesses, word)

        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue
        if guess in correct_guesses or guess in missed_guesses:
            print("You already guessed that.")
            continue

        if guess in word:
            correct_guesses.append(guess)
            if all(letter in correct_guesses for letter in word):
                display_board(missed_guesses, correct_guesses, word)
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            missed_guesses.append(guess)
            if len(missed_guesses) == len(HANGMAN_PICS) - 1:
                display_board(missed_guesses, correct_guesses, word)
                print(f"You ran out of guesses. The word was: {word}")
                break

if __name__ == "__main__":
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break
