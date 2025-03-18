list = [
    '''apple''', '''banana''', '''cherry''', '''dragonfruit''', '''elephant''',
    '''flamingo''', '''grapefruit''', '''honeydew''', '''iguana''', '''jellyfish''',
    '''kangaroo''', '''lemonade''', '''mango''', '''nectarine''', '''octopus''',
    '''penguin''', '''quokka''', '''raspberry''', '''strawberry''', '''tangerine''',
    '''umbrella''', '''volcano''', '''walrus''', '''xylophone''', '''yak''', '''zebra'''
    ]


import random
from words import list
from art import logo, stages
import sys

lives = 6

your_word = random.choice(list)
placeholder = "_" * len(your_word)

print(logo)
print('---------------------------------------------------')
print(f"Here comes your word /// {placeholder} /// \nTry to guess it, but do be aware, you have {lives} lives."
      f" \n---------------------------------------------------")

game_over = False
correct_guesses = []

while not game_over:
    user_input = input("Enter a letter: ").lower()



    if user_input in correct_guesses:
        print("You already guessed that letter!")
        continue

    display = ""

    for letter in your_word:
        if letter == user_input:
            display += letter
            correct_guesses.append(user_input)
        elif letter in correct_guesses:
            display += letter
        else:
           display += "_"

    if user_input not in your_word:
        lives -= 1
        print(f'Shame... You lost a life, you have {lives} lives left.')

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE, THE WORD WAS {your_word}.upper **********************")


    print(display)
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

