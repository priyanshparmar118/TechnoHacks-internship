import random
option = ("rock", "paper", "scissor")
player = input("Enter your choice : ")
computer = random.choice(option)

print("Player: ",player)
print("Computer: ",computer)

if player == computer:
    print("It's a draw")
    print("Thanks for playing")
elif player == "rock" and computer == "scissor":
    print("You win")
    print("Thanks for playing")

elif player == "paper" and computer == "rock":
    print("You win")
    print("Thanks for playing")

elif player == "scissor" and computer == "paper":
    print("You win")
    print("Thanks for playing")

else:
    print("You lose! Computer win")
    print("Thanks for playing")