
# Password_Generator by user input

# import the random libr for random value

import random
import string

def generate_password(length):

    # Define the character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by choosing characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            # the user to specify the length of the password
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length must be at least 1.")
                continue
            
            # Generate and display the password
            password = generate_password(length)
            print(f"Generated Password: {password}")

        except ValueError:
            print("Invalid input. Please enter a positive integer.")

        # Ask if the user wants to generate another password
        play_again = input("Do you want to generate another password? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for using the Password Generator!")
            break

if __name__ == "__main__":
    main()