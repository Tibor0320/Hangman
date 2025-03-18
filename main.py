# Import necessary libraries
import random
import sys
from words import list  # Import word list for the game
from art import logo, stages  # Import ASCII art for game visuals


# Set initial number of lives
lives = 6

# Choose a random word from the list and create hidden display
your_word = random.choice(list)
placeholder = "_" * len(your_word)  # Create underscores matching word length

# Display game logo and welcome message
print(logo)
print('---------------------------------------------------')
print(f"Here comes your word /// {placeholder} /// \nTry to guess it, but do be aware, you have {lives} lives."
      f" \n---------------------------------------------------")

# Initialize game state variables
game_over = False  # Controls the game loop
correct_guesses = []  # Keeps track of correctly guessed letters

# Main game loop
while not game_over:
    # Get player input and convert to lowercase
    user_input = input("Enter a letter: ").lower()

    # Check if letter was already guessed
    if user_input in correct_guesses:
        print("You already guessed that letter!")
        continue  # Skip the rest of the loop and start next iteration

    # Initialize empty display string for current round
    display = ""

    # Process each letter in the target word
    for letter in your_word:
        if letter == user_input:  # Current guess matches letter
            display += letter
            correct_guesses.append(user_input)
        elif letter in correct_guesses:  # Letter was previously guessed
            display += letter
        else:  # Letter hasn't been guessed yet
            display += "_"

    # Handle incorrect guess
    if user_input not in your_word:
        lives -= 1  # Reduce remaining lives
        print(f'Shame... You lost a life, you have {lives} lives left.')

        # Check if player has lost
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE, THE WORD WAS {your_word} *********************")
            sys.exit()



    # Show current state of word
    print(display)

    # Check if player has won
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        sys.exit()



    # Display current hangman stage
    print(stages[lives])
