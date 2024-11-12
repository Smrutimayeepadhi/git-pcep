
"""#subscripting
print("Hello"[0])
#string
print("123"+"847")
#whole number
print(23 + 45)
#large number: computer understand large numbers by "_" e.g: 782,23,00
print(782_23_00)
#floating number
print(3.14159)
# Boolean
print(True)
print(False)
print((int(34)+ int(45 )))
x = input("enter your name.")
y: int = len(type(x))
print("Number of letters in your name: " + y )

bmi = 84 /1.65**2
print(bmi)
print(round(bmi))
print(round(bmi, 2))#it will print 2 decimal point"""



#TIP CALCULATOR
print("Welcome to tip calculator!")
total_bill = float(input("What was the total bill? £"))
tip = int(input("How much percentage of tip would you like to give? 10, 12 0r 15?" ))
split_people =int(input("How many people to split the bill? "))
tip_with_bill = total_bill+ (total_bill*tip)/100

pay = tip_with_bill/split_people
final_bill = round(pay, 2)

print(f'Each person should pay: £{pay} .')







