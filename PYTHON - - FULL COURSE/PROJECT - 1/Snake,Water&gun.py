import random

def game(user_input, computer_input):
    if user_input == computer_input:
        print("It's a tie")
    elif user_input == "snake" and computer_input == "water":
        print("User won")
    elif user_input == "water" and computer_input == "snake":
        print("Computer won")
    elif user_input == "gun" and computer_input == "water":
        print("Computer won")
    elif user_input == "water" and computer_input == "gun":
        print("User won")
    elif user_input == "snake" and computer_input == "gun":
        print("Computer won")
    elif user_input == "gun" and computer_input == "snake":
        print("User won")

choices = ["snake", "water", "gun"]
computer_input_choice = random.choice(choices)
user_input_choice = input("Enter snake, water or gun: ").lower()

if user_input_choice not in choices:
    print("Invalid input!")
else:
    print("Computer chose:", computer_input_choice)
    game(user_input_choice, computer_input_choice)



#Other Way

import random

# Choices available
choices = ["snake", "water", "gun"]

# Dictionary: key defeats value
winning_rules = {
    "snake": "water",
    "water": "gun",
    "gun": "snake"
}

# Computer chooses randomly
computer_choice = random.choice(choices)

# User input
user_choice = input("Enter snake, water, or gun: ").lower()

# Validate input
if user_choice not in choices:
    print("Invalid input! Please enter snake, water, or gun.")
else:
    print(f"\nComputer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a Tie!")

    elif winning_rules[user_choice] == computer_choice:
        print("🎉 You Win!")

    else:
        print("💻 Computer Wins!")
