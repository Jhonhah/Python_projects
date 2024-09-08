import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from words import word_list

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from art import logo, stages
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************<???>{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""
    if guess in correct_letters:
        print("***********************You have already guessed this letter***********************")
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"***********************{guess} is not in the chosen word***********************")

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************\n The word is {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
