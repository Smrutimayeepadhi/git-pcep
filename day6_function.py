#def = defining your own function
"""
Randomly choose a word_list assign to a variable. then print it.
ask the user to guess a letter and assign to their variable called guess.make guess lowercase.
check if the letter the user guessed(guess) is one of the letters in the chosen word.
print 'right if it is ,print 'wrong if it's not.'
"""
import random
word_list = ["Chacha", "Tutu", "Rosy"]
chosen_word = random.choice(word_list)
print(chosen_word)

user_guess = input("guess a letter: ").lower
for letter in chosen_word:
    if letter == user_guess:
        print("right")
    else:
        print("wrong")


        








































