# Hangman-Game
This Python script implements a simple Hangman game where the player has to guess a randomly chosen word by suggesting letters.
How the Code Works
A predefined list of words is stored in words. The program selects one at random.
The chosen word is hidden by underscores (_), representing unguessed letters.
The player has six chances to guess the word before losing.
The player inputs a single letter at a time. If the letter is in the word, it is revealed in its correct positions. Otherwise, the number of wrong guesses increases.
The game continues until the player either:
Guesses the entire word → Wins
Uses up all six wrong guesses → Loses
Features and Rules
✔ Random word selection
✔ Tracks guessed letters to prevent duplicate inputs
✔ Validates input (only single letters allowed)
✔ Displays progress after each guess
✔ Ends the game when the word is guessed or attempts run out

This is a simple yet fun game that demonstrates basic Python concepts like loops, conditionals, lists, and string manipulation. 🚀
