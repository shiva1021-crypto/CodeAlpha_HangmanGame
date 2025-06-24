import random

# List of words with hints
words_with_hints = {
    'python': 'A popular programming language.',
    'hangman': 'The name of this game.',
    'intern': 'A person undergoing training.',
    'program': 'A set of instructions for a computer.',
    'codealpha': 'The company offering this internship.'
}

def play_game():
    word_to_guess = random.choice(list(words_with_hints.keys()))
    hint = words_with_hints[word_to_guess]
    guessed_letters = []
    max_attempts = 6
    attempts_left = max_attempts

    print("\n🎮 New Game: Hangman")
    print("Hint:", hint)
    print(f"You have {max_attempts} incorrect guesses.")

    while attempts_left > 0:
        display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print("\nWord:", display_word)
        print("Guessed letters:", ' '.join(guessed_letters))

        if all(letter in guessed_letters for letter in word_to_guess):
            print("\n🎉 Congratulations! You guessed the word correctly:", word_to_guess)
            return

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⛔ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts_left -= 1
            print(f"❌ Wrong guess. Attempts left: {attempts_left}")
        else:
            print("✅ Correct guess!")

    print("\n💀 Game Over! The word was:", word_to_guess)

# Game loop
while True:
    play_game()
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay != 'yes':
        print("Thanks for playing! 👋")
        break
