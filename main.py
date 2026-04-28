import random #importing random module

while True: #iterate loop
    user_action = input("Enter either - Rock, Paper or Scissors") #take input
    possible_actions = ["Rock", "Paper", "Scissors"]
    #using random fucntion
    computer_action = random.choice(possible_actions)
    print(f"\nYou choose {user_action}, computer choose{computer_action}.\n") #Display both outputs what is selected by you and the computer

#conditions to check who won the game
    if user_action == computer_action:
        print(f"Both of the players selected {user_action}. It's a Tie!!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes Scissors! You win!!")
        else:
            print("Paper covers Rock! You lose!!") 


    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock! You win!!")
        else:
            print("Scissors cut Paper! You lose!!") 


    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cut Paper! You win!!")
        else:
            print("Rock smashes Scissors! You lose!!") 

#take input to play again
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break