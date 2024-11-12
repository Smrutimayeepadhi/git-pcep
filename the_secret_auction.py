

print("*WELCOME TO BLIND AUCTION*")




def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of £{highest_bid}.')

continue_bidding = True
input_dictionary = {}
while continue_bidding:
    name_input = input("what is your name: ")
    bid_price = int(input("what is your bid price: £"))
    #input_dictionary = {name_input:bid_price}
 #OR you can write it like this way
    input_dictionary[name_input]= bid_price
    other_user = input("Is there any other use who want to bid? Type 'yes' or 'no'  ").lower()
    if other_user == "no":
        continue_bidding = False
        find_highest_bidder(input_dictionary)
    elif other_user == 'yes':
        print("\n" *15)





