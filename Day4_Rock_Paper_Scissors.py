import random
rock = "ROCK"
paper = "PAPER"
scissors = "SCISSORS"
user_choice =int(input(" choose your number 0 for rock or 1 for paper or 2 for scissors: "))
#0, 1, 2
computer_choice = random.randint(0, 2)
print(f'computer chose {computer_choice}.')

if user_choice >=3 or user_choice < 0:
    print("invalid number! try again.")
elif user_choice ==0 and computer_choice == 2:
    print("You win!")
elif computer_choice ==0 and user_choice ==2:
    print("you lose!")
elif user_choice > computer_choice:
    print("you lose!")
elif computer_choice > user_choice:
    print(" you win!")
elif computer_choice == user_choice:
    print("it's draw!")







