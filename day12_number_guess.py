from random import randint
easy_level = 5
hard_level = 10

def difficulty_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level.lower == "easy":
        return easy_level
    else:
       return hard_level
#function to check users' guess against the actual answer
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("too high!")
        return turns - 1
    elif user_guess < actual_answer:
        print("too low!")
        return turns -1
    else:
        print(f'You got it! The answer is {actual_answer}')

def game():
    print("Welcome to number guessing problem!")
    print("I'm thinking a number between 1 to 100. ")

    #choosing a random number 1 to 100.
    choose = randint(1, 100)#both 1 and 100 can show up
    print(choose)
    difficulty_level()
    #repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != choose:
        guess = int(input("Guess a number: "))
        check_answer(user_guess = guess, actual_answer= choose)
game()






