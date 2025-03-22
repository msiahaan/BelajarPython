import random

def get_user_choice():
    print("Choose one: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose again.")
        user_choice = input("Your choice: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return 0
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return 1
    else:
        return -1

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result= determine_winner(user_choice, computer_choice)
    if result == 1:
        print("You win!")
    elif result == 1:
        print("You lose!")
    else:
        print("It's a tie!")
    total_score += result
    print("Total score:", total_score)

if __name__ == "__main__":
    continue_playing = True
    while continue_playing:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        continue_playing = play_again == "yes"
    print("Thanks for playing!")