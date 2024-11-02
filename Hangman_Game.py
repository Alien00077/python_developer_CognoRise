import random

def hangman():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(word_list)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()

    while attempts > 0:
        print("\nCurrent word:", ' '.join(guessed_word))
        guess = input("Guess a letter: ")

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")

        if "_" not in guessed_word:
            print("Congratulations! You've won. The word was:", word)
            return

    print("You lost! The word was:", word)

hangman()
