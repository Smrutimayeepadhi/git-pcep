"""fruits = ["apple","peach", "pear"]
for fruit in fruits:
    print(fruit)# once this line loop finished the control jumps to next line
    print(fruit + " pie")

print(fruits)"""
"""student_scores = [23, 45,102, 56, 67, 78, 89, 100]
'''total_score = sum(student_scores)
print(total_score)'''
max_score = 0
for score in student_scores:
    print(score)
    if score > max_score:
        max_score = score
print(max_score)
#range function with for loop
total = 0
for number in range(1, 11):
    if total>number:
        total+=number
        print(number)"""

#PROJECT
import random

print("Welcome to the PyPassword generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*',]
user_letters = int(input("How many letters would you like in your password?\n "))
user_symbols = int(input("How many symbols would you ? \n"))
user_numbers = int(input("How many numbers would you like in your password?\n "))
#easy level
"""password = ""
for i in range(0, user_letters):#let's say user wil put 4 it will be 4+1=5 where range will take 1-
    password += random.choice(letters)
for i in range(0, user_symbols):
    password += random.choice(numbers)
for i in range(0, user_numbers):
    password +=random.choice(symbols)
print(f'Your password is {password} ')"""
#Hard level
password_list = []
for i in range(0, user_letters):#let's say user wil put 4 it will be 4+1=5 where range will take 1-
    password_list.append(random.choice(letters))
for i in range(0, user_symbols):
    password_list.append(random.choice(numbers))
for i in range(0, user_numbers):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
password = ""
for i in password_list:
    password = password+i


print(f'Your password is {password} ')


