print("Welcome to Python Pizaa Deliveries! ")
size = input("What size of pizza do you want? S, M, L: ")
print("small_pizza = 15")
print("medium_pizza = 20")
print("large_pizza = 25")
peporroni = input("would you like add some pepporoni on your pizza cost of £2? 'yes' or 'no'")

bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25
if peporroni == "yes":

    small_pizza = 2
    medium_large = 3
    if(peporroni == small_pizza):
        bill+=small_pizza
    else:
        bill += medium_large
else:
    print("okay")

cheese = input("do you want add some extra cheese cost of £1? 'yes' or 'no'")
if cheese == "yes":
    bill +=1
else:
    print("alright")

print(f'your total bill is {bill}.')
print("Thank you!")





