"""
Create a functional drive thru
"""


def get_item(x):
    if x == 1:
        return "Here's your Cheeseburger"
    elif x == 2:
        return "Here's your Fries"
    elif x == 3:
        return "Here's your Soda"
    elif x == 4:
        return "Here's your Ice Cream"
    elif x == 5:
        return "Here's your Cookie"
    else:
        return "invalid option"


def welcome():
    print("Welcome to Sonnyboy's Diner!")
    print("Here's the menu:")
    print("1. Cheeseburger")
    print("2. Fries")
    print("3. Soda")
    print("4. Ice Cream")
    print("5. Cookie")


welcome()

option = int(input("What would you like to order? (1-5): "))
print(get_item(option))
