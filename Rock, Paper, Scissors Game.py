# welcoming player to the game
print('Welcome to Rock, Paper, and Scissors Game!')

import random

while True:
    print()
    users_choice = input("Enter a choice (rock, papers, scissors): ")
    possible_outcomes = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_outcomes)


# if the player and computer's choices are the same
    if users_choice == computer_action:
        print('The Player selected', users_choice, ',', 'the computer selected', computer_action)
        print()
        print("It's a Tie! Both Players selected", users_choice)

# if the player's choice is rock and the computer's choice is scissors
    elif users_choice == 'rock':
        if computer_action == 'scissors':
            print('The Player selected', users_choice, ',', 'the computer selected', computer_action)
            print()
            print('You win! Congratulations!')

# the player would lose if it's paper, if same choices then it's a tie (it will be executed first)
        else:
            print('The Player selected', users_choice, ',', 'the computer selected', computer_action)
            print()
            print("Sorry! You lose!")

# if the player's choice is paper and the computer's choice is rock
    elif users_choice == 'paper':
        if computer_action == 'rock':
            print('The Player selected', users_choice, ',', 'the computer selected', computer_action)
            print()
            print('You win! Congratulations!')

# the player would lose if it's scissors, if same choices then it's a tie (it will be executed first)
        else:
            print('The Player selected', users_choice, ',', 'the computer selected', computer_action)
            print()
            print("Sorry! You lose!")

# if the player's choice is scissors and the computer's choice is paper
    elif users_choice == 'scissors':
        if computer_action == 'paper':
            print('The Player selected', users_choice, ',', 'the computer selected', computer_action)
            print()
            print('You win! Congratulations!')

# the player would lose if it's rock, if same choices then it's a tie (it will be executed first)
        else:
            print('The Player selected', users_choice, ',', 'the computer selected', computer_action)
            print()
            print("Sorry! You lose!")

# if the player's choice is to quit from the game
    elif users_choice == 'quit':
        print("Thanks for playing!")
        break

# if the player's choice is not a valid option from the choices
    elif users_choice not in possible_outcomes:
        print("Invalid choice! Please select a valid option in the three choices.")
        continue