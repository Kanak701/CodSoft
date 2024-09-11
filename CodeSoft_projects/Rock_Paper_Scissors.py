
# Making a Game of Rock-Paper-Scissor 

# import required library

import random

 #the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']  
    return random.choice(choices)  # Randomly choice the list

# Function to determine the winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'  # If both choices are the same, it's a tie
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'  # User wins based on the rules
    else:
        return 'computer'  # Computer wins in other cases

# Func to play the game
def play_game():
    print("Welcome to Rock-Paper-Scissors!")  # Wlco message

    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()  # Get user choice
        if user_choice not in ['rock', 'paper', 'scissors']:  # Check if the valid input 
            print("Invalid choice, please try again.")
            continue  # Ask for input again if invalid

        computer_choice = get_computer_choice()  # computer's choice
        print(f"Computer chose: {computer_choice}")  # Display the computer's choice

        winner = get_winner(user_choice, computer_choice)  # Determine the winer

        if winner == 'user':
            print("You win!")  # User wins
        elif winner == 'computer':
            print("Computer wins!")  # Computer wins
        else:
            print("It's a tie!")  # tie

        play_again = input("Do you want to play again? (yes/no): ").lower()  # Ask if the user wants to play again
        if play_again != 'yes':  # If the answer is not 'yes', exit the loop
            print("Thanks for playing!") 
            break  # Exit the loop

# Start the game if this script is run directly
if __name__ == "__main__":
    play_game()