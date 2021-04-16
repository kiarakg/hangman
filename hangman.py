import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)     # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

# keeping track of letters we've guessed, correctly guessed, and what is and isn't a valid letter
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)     # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()     # what the user has guessed


