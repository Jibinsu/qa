import random

def play_round():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "rock":
        if computer_choice == "paper":
            return "computer"
        else:
            return "user"
    elif user_choice == "paper":
        if computer_choice == "scissors":
            return "computer"
        else:
            return "user"
    elif user_choice == "scissors":
        if computer_choice == "rock":
            return "computer"
        else:
            return "user"
    else:
        return "invalid"

rounds_played = 0
user_wins = 0
computer_wins = 0
ties = 0

play_again = True
while play_again:
    rounds_played += 1
    result = play_round()

    if result == "user":
        user_wins += 1
        print("You win!")
    elif result == "computer":
        computer_wins += 1
        print("Computer wins!")
    elif result == "tie":
        ties += 1
        print("It's a tie!")
    else:
        print("Invalid choice!")

    print("Rounds played: {}".format(rounds_played))
    print("User wins: {}".format(user_wins))
    print("Computer wins: {}".format(computer_wins))
    print("ties: {}".format(ties))


    play_again_input = input("Do you want to play another round? (yes/no): ")
    if play_again_input == "no":
        print ("thankyou for playing, see ya next time: ")
    else:
        print ("do you feel lucky punk?")
    play_again = play_again_input.lower() == "yes"
