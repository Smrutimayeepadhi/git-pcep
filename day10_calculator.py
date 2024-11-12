#CALCULATOR PROJECT



def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = { "+": add, "-": sub, "*":mul, "/":div, }
#a = operations["*"](4, 8)
# print(a)
def calculator():

    should_accumulate = True
    user_num1 = float(input("What is your first number?  "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick your operator: ")
        #program asks the user to type second number
        user_num2 =  float(input("what is your second number? "))

        #program works out the result based on the chosen mathematical operator
        result = operations[operation_symbol](user_num1, user_num2)
        #print the operation to the user
        print(f'{user_num1} {operation_symbol} {user_num2} = {result}')

        #program asks if the user wants to continue working with previous result
        next_operation = input(f"type 'y' if you to continue with {result} or type 'n' to start a new calculation.")
        if next_operation == "y":
            user_num1 = result
        else:
            should_accumulate = False
            print("\n" * 10)
        calculator()



calculator()

