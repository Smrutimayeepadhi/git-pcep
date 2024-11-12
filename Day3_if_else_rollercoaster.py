"""print("Welcome to roller coaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster.")
else:
    print("sorry, you can't ride the rollercoaster.")

#Check if the number in the input area is odd or even.if it's odd print "ODD" otherwise "even"
user_input = int(input("Enter a number: "))

if(user_input % 2 == 0):
    print("It's a even number.")
else:
    print("It's a odd number.")

#Check if child is <=18 year old he/she needs to pay £7 otherwise >18, needs to pay £12
age = int(input("How old are you? "))
if(age <= 18):
    print("you need to pay: £7 ")
else:
    print("you need to pay: £12 ")

#We will write above program by using nested-if statementsprint("Welcome to roller coaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you? "))
    if (age <= 12):
        print("you need to pay: £5 ")
    elif(age <=18):
        print("you need to pay: £7 ")
    else:
        print("you need to pay: £12 ")

else:
    print("sorry, you can't ride the rollercoaster.")"""
#Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

"""If the bmi is under 18.5 (not including), print out "underweight"

If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

If the bmi is 25 (including) or over, print out "overweight"""

"""weight = 85
height = 1.85

bmi = float(weight / (height ** 2))
if (bmi < 18.5):
    print("underweight")

elif (bmi<25):
    print("normal")
elif (bmi >= 25):
    print("overweight")

else:
    print("Obesity")"""

print("Welcome to roller coaster!")
height = int(input("What is your height in cm? "))
pay = 0
if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("what is your age? "))
    if(age < 12):
        pay = 5
        print(f'you need to pay £5.')
    elif(age<18):
        pay = 7
        print("you need to pay £7.")
    else:
        pay = 12
        print("you need to pay £12. ")
        want_photo = input("would you like a photo? 'yes' or 'no'")
        if want_photo == "yes":
            pay += 3
    print(f'the total bill is {pay}')


else:
    print("sorry, you can't ride the rollercoaster.")























