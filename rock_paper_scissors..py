import random
choices = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Ensure user enters a valid choice
if user_choice not in choices:
    print("Invalid choice. Please enter rock, paper, or scissors.")
else:
    # Computer makes a random choice
    computer_choice = random.choice(choices)
    
    # Display the choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors"):
        print("You win!")
    elif (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    elif (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")