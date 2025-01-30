import random

def hangman():
    words = ["chicken", "mouse", "computer", "application", "python", "programming", "keyboard", "internet"]
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6
    word_completion = "_" * len(word)

    print("Welcome to Hangman Game!")
    print(f"You have {max_wrong_guesses} wrong guesses.")
    print("The word to guess is:", ' '.join(word_completion))

    while max_wrong_guesses > wrong_guesses and "_" in word_completion:
        guess = input("guess tha letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("please enter single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            # Update word completion
            word_completion = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        else:
            wrong_guesses += 1
            print("Incorrect guess. You have", max_wrong_guesses - wrong_guesses, "guesses left.")

        print("Current word:", ' '.join(word_completion))

    if '_' not in word_completion:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Sorry, you've run out of guesses. The word was:", word)

    
if __name__ == "__main__":
    hangman()