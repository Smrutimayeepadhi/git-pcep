MENU = {
    "espresso": {
        "ingredients":{
            "coffee":18,
            "water":50,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients":{
            "coffee":24,
            "water":200,
            "milk":150,
        },
        "cost": 2.5
    },
    "cappuccino":{
        "ingredients":{
            "coffee":24,
            "water":250,
            "milk":100,
        },
        "cost": 3.0
    }
}
price = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#TODO: 1.prompt user by asking "what would you like?(espresso/latte/cappuccino)" and after coffee dispensed ask for next customer
#TODO: 2. turn off the coffee machine by entering "off" to the prompt
def is_resource_sufficient(order_ingredient):
    is_enough = True
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f'sorry, there is no enough{item}')
            is_enough = False
    return is_enough
def process_coins():
    """returns the inserted calculated coins"""
    print("please insert coins.")
    total = int(input("how many quarters: ")) * 0.25
    return total
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        """round to two decimal numbers"""
        change = round(money_received - drink_cost, 2)
        print(f'Here is the {change} in change.')
        global price
        price += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. money refunded.")
        return False
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for i in order_ingredients:
        resources[i] = resources[i] - order_ingredients[i]
    print(f'Here is your drink {drink_name}☕️.Enjoy!')
is_on = True
while is_on:
    choice = str(input("what would you like?(espresso/latte/cappuccino): "))
    if choice == "off":
        is_on = False
    elif choice == "report":
            print(f'water: {resources["water"]}ml')  # option+shift button ->for multiline editing(u will get multi cursors)
            print(f'milk: {resources["milk"]}ml')
            print(f'coffee: {resources["coffee"]}g')
            print(f'money: £{price}')

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(money_received=payment,drink_cost=drink["cost"]):
                make_coffee(drink_name= choice,order_ingredients=drink["ingredients"])
#TODO: 3.print report: when he user enters "report" to the prompt which should be generated the current resource values
