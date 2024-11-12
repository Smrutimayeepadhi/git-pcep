"""year = int(input("what is your birth year? "))

if 1980< year < 1994:
    print("You are millennial.")
elif year >= 1994:
    print("you are gen z.")"""

"""pages = int(input("number of pages = "))
word_per_page = int(input("number of words = "))
total_words = pages * word_per_page

print(f"Total number of words = {total_words}")"""

"""def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
print(odd_or_even(8))"""

"""def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(leap_year(2024))"""

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print(number)
fizz_buzz(15)