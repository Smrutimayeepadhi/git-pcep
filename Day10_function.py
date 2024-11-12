#function is a block of code to which you can trigger it multiple times when you need without re-write or copypaste it.
#The content of the function must be indented to signal it's inside.
"""def format_name(first_name,last_name):
    f_name = input(first_name).title()
    l_name =input(last_name).title()
    return f'your name is {f_name} {l_name}'
print(format_name(first_name= "f_name", last_name= "l_name"))"""

"""def function_1 (text):
    return text + text
def function_2(text):
    return text.title()
output = function_2(function_1("hello"))
print(output)"""

#more than one return key_word
"""def format_name(first_name,last_name):
    f_name = input(first_name).title()
    l_name =input(last_name).title()
    return f'your name is {f_name} {l_name}'
print(format_name(first_name= "f_name", last_name= "l_name"))"""



year =int(input("put a year: "))
def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0:
        print("its a leap year.")
    else:
        print("its not a leap year.")
is_leap_year(year)
