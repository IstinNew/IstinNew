# -*- coding: utf-8 -*-
"""SimpleHangman.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tY_VZ7mNZCD_mE_nNR8wllqc2T5P2G7I

### Hangman game

Welcome to the Simple Hangman Game! I invite you to crack the words 🙌

This notebook hosts a basic, fun and engaging Hangman game implemented in Python.

*Enjoy the Game! Dive into the code and enjoy playing the Hangman game. It’s a great way to have fun while practicing Python skills!*
"""



"""### About the Game

1. Run the code in each cell.
2. The game will generate a random tech-themed word.
3. You will be prompted to guess a letter.
4. The game will check if your guessed letter is in the word and provide
   feedback.
5. Keep playing, keep guessing

Follow the prompts to guess letters.

### Sample

Hidden word is: _ _ _ _ _ _ _ _
Guess a letter: E
Oh no, that's a miss! Try again. ❌

Guess a letter: P
Bingo! The letter P is in the word! 🎉

...

Hooray! You've cracked it: PYTHONIC 🎊
"""

# Simple Hangman Game in Python
import random

# Function to get a unique tech-themed word
def get_unique_word():
    words = ["ALGORITHM", "CODING", "DATABASE", "INNOVATION", "JUPYTER", "PYTHONISTA"]
    return random.choice(words)

# Get the answer word
answer_word = get_unique_word()

# Create the hidden word with underscores and spaces
hidden_word = " ".join("_" for _ in answer_word)

# Print the hidden word
print(f"Hidden word is: {hidden_word}")

# Take user input for a letter
picked_letter = input("Guess a letter: ").upper()

# Check if the picked_letter is in the answer_word
if picked_letter in answer_word:
    print(f"Bingo! The letter {picked_letter} is in the word! 🎉")
else:
    print("Oh no, that's a miss! Try again. ❌")
