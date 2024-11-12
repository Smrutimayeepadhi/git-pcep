"""def greet():
    print("hi")
    print("hello")
    print("namaskar")
greet()
#function that allows input

def greet_with_input(name):
    print(f'hi {name}')
    print(f'hello {name}')
    print(f'namaskar{name}')

greet_with_input("Smruti")



user_age = int(input("what is your age? "))
no_of_weeks_you_have_left = 90 - user_age
x = no_of_weeks_you_have_left*12*4
def life_in_weeks():
    print(f"if you live until 90 years old, {x} weeks you have left.")
life_in_weeks()"""

#function with more than 1 input
"""def greet_with(name, location):
    print(f'user1: {name},{location}')
greet_with("Himanjan", "london")
greet_with("Smruti", "london")
greet_with("Shanvi","london")"""

"""def multiple_parameter(name, location):
    print(f'Hello {name}!')
    print(f'what it is like in {location}.')
multiple_parameter("Smruti", "london")
#or
multiple_parameter(location ="london", name="Smruti")"""


"""Love Calculator
💪 This is a difficult challenge! 💪 

You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 
Total = 5 

L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 

Total = 3 
Love Score = 53
Example Input 
calculate_love_score("Kanye West", "Kim Kardashian")

Example Output
42"""
#user = input("what is your name? ")
#partner_name = input("what is your partner name?  ")
user_name = input("what is your name? ")
partner_name = input("what is your partner name?  ")
true =["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]
con_true_love = true+love
print(con_true_love)

def calculate_love_score(user_name, partner_name):
    concatenate_name = user_name + partner_name
    print(concatenate_name)
    list_letter =[]
    """for letter in concatenate_name:
        list_letter.append(letter)
    print(list_letter)
    #count = 0
    #for each in concatenate_name & list_letter:
        #if concatenate_name == list_letter:
    for letter in concatenate_name:
        if letter in list_letter[]:
            print("it is")"""








calculate_love_score(user_name,partner_name)


