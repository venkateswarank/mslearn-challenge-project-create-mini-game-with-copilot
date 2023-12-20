# write a function that accepts user input from command line based on 3 options - rock, paper or scissors
# generate a random choice from the computer
# compare the two choices and determine a winner
# print the results to the user
# allow the user to play again
# if the user quits, print the number of wins and losses

import random

# define 2 global variables to keep track of wins and losses
wins = 0
losses = 0

def play_game():
    global wins
    global losses
    user_choice = input("Choose rock, paper or scissors: ")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
            wins += 1   
        else:
            print("You lose!")
            losses += 1
    else:
        print("Invalid input. Try again.")
    play_again = input("Play again? (y/n): ")
    if play_again == "y":
        play_game()
    else:
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")

play_game()
