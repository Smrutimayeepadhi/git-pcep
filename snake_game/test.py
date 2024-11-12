a = int(input("How many days ago have you purchased the item? "))
b = input("Have you used the item at all [y/n]? ")
c = input("Has the item broken down on its own [y/n]? ")
def online_store(p, q, r):

    if a <= 10 and b == "n" and c == "y":
        return True
    return False


online_store()