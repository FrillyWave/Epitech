import random
from english_words import *

def game_over(penalties):
    if penalties >= 12:
        print("You lose!")

def get_random_item(s):
    return random.choice(list(s))

random_word = get_random_item(get_english_words_set(['web2'], lower=True))


def get_underscore(word):
    return ["_ "] * len(word)

def main():
    penalties = 0
    solved = False
    word_to_guess = random_word
    under_scored_word = get_underscore(word_to_guess)
    while not game_over(penalties) or solved:
        print(word_to_guess)
        print(" ".join(under_scored_word))
        letter = input("Enter a letter : ")
        if letter in word_to_guess :
            for i, char in enumerate(word_to_guess):
                if letter == char:
                    under_scored_word[i] = letter
            if '_' not in under_scored_word:
                solved = True
        else:
            penalties += 1
        
        if solved == True:
            print(f"Bravo, le mot était {word_to_guess}")

main() 