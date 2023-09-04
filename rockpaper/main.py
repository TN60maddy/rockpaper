import random
options = ("rock", "paper", "scissors")
playing = True
while playing:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("\nTie")
    elif player == "rock" and computer == "scissors":
        print("\nYOU WIN!!!")
    elif player == "scissors" and computer == "paper":
        print("\nYOU WIN!!!")
    elif player == "paper" and computer == "rock":
        print("\nYOU WiN!!!")
    else:
        print("\nYOU LOSE!!!")
    play_again = input("Play Again? (y/n): ").lower()
    if not play_again == "y":
        playing = False
        
print("Thanks For Playing!!!")